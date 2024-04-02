class Chatbot {
  constructor (domainOrigin, user) {
    this.domainOrigin = domainOrigin
    this.user = user
    this.messages = []
    this.questionBank = []
    this.responses = []
    this.waitingUserReply = false
    this.collectedUserResponses = []
  }

  getTimestamp () {
    const now = new Date()
    const hours = now.getHours().toString().padStart(2, '0') // Ensure 2 digits
    const minutes = now.getMinutes().toString().padStart(2, '0') // Ensure 2 digits
    return `${hours}:${minutes}`
  }

  sleep (time) {
    // time is in ms
    return new Promise(resolve => setTimeout(resolve, time))
  }

  addMessageToChat (sender, body, responses = []) {
    this.messages.push({
      sender: sender,
      body: body,
      responses: responses,
      timestamp: this.getTimestamp()
    })
  }
  async checkUserSignedIn () {
    if (!this.user.loggedIn) {
      await this.sleep(1000)
      this.addMessageToChat('bot', 'Please sign in to continue!')
      this.waitingUserReply = true
      // Wait for user reply asynchronously
      await new Promise(resolve => {
        const intervalId = setInterval(() => {
          if (!this.waitingUserReply && this.user.loggedIn) {
            clearInterval(intervalId)
            resolve()
          }
        }, 100) // Check every 100 milliseconds for user reply
      })
    }
  }

  async startWelcomeChat () {
    console.log('Starting chat...')
    await this.startChat()
    console.log('Finished chat...')
    await this.checkUserSignedIn()
    this.apiGetQuestionBank('initial_survey_question_bank')
    await this.sleep(1500)
    await this.startChat()
  }

  async startChat () {
    for (let i = 0; i < this.questionBank.length; i++) {
      await this.sleep(1500)
      this.addMessageToChat('bot', this.questionBank[i]['body'], this.questionBank[i]['responses'])
      this.responses = this.questionBank[i]['responses']
      if (this.questionBank[i]['response_required']) {
        this.waitingUserReply = true
        // Wait for user reply asynchronously
        await new Promise(resolve => {
          const intervalId = setInterval(() => {
            if (!this.waitingUserReply) {
              clearInterval(intervalId)
              resolve()
            }
          }, 100) // Check every 100 milliseconds for user reply
        })
      } else {
        await this.sleep(1000)
      }
    }
    console.log('out the for loop')
  }

  async handleUserReply (userReply) {
    const lastMessage = this.messages[this.messages.length - 1]
    this.addMessageToChat('user', userReply)
    if (lastMessage.chatgpt_reply) {
      const chatGptResponse = await this.apiGetChatGptResponse(
        userReply,
        lastMessage,
        this.user.name
      )
      this.addMessageToChat('bot', chatGptResponse)
    }
    this.waitingUserReply = false
  }

  apiGetQuestionBank (requestedQuestionBank) {
    console.log('In apiGetQuestionBank')
    return new Promise((resolve, reject) => {
      const payload = {}
      payload.questionBank = requestedQuestionBank

      const requestOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      }

      const url = this.domainOrigin + '/api/chatbot/question_bank'

      fetch(url, requestOptions)
        .then(response => response.json())
        .then(apiObject => {
          try {
            if (apiObject.rc == 0) {
              this.questionBank = apiObject.chatbot_questions
              resolve(apiObject.message)
            } else {
              console.log(`Failed to get question bank ${apiObject.message}`)
            }
          } catch (error) {
            console.log(error)
            reject(error)
          }
        })
        .catch(error => {
          console.log(error)
          reject(error)
        })
    })
  }

  apiGetChatGptResponse (userReply, previousQuestion, userName) {
    console.log('In apiGetReplyFromChatbot')

    return new Promise((resolve, reject) => {
      const payload = {}
      if (userReply != null) {
        payload.user_reply = userReply
        payload.previous_question = previousQuestion
        payload.user_name = userName

        this.pushUserReplyToMessages(userReply)
      }

      const requestOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      }

      const url = this.domainOrigin + '/api/chatgpt/response'

      fetch(url, requestOptions)
        .then(response => response.json())
        .then(apiObject => {
          try {
            if (apiObject.rc == 0) {
              resolve(apiObject.chat)
            } else {
              console.log('Failed to get chatgpt reply')
            }
          } catch (error) {
            console.log(error)
            reject(error)
          }
        })
        .catch(error => {
          console.log(error)
          reject(error)
        })
    })
  }
}

export default Chatbot
