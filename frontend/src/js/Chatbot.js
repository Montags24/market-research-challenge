class Chatbot {
  constructor (domainOrigin) {
    this.domainOrigin = domainOrigin
    this.messages = []
  }

  getTimestamp () {
    const now = new Date()
    const hours = now.getHours().toString().padStart(2, '0') // Ensure 2 digits
    const minutes = now.getMinutes().toString().padStart(2, '0') // Ensure 2 digits
    return `${hours}:${minutes}`
  }

  pushUserReplyToMessages (userReply) {
    this.messages.push({
      sender: 'user',
      body: userReply,
      responses: [],
      timestamp: this.getTimestamp()
    })
  }

  apiGetNextResponseFromChatbot (messageId) {
    console.log('In apiGetNextResponseFromChatbot')
    return new Promise((resolve, reject) => {
      const payload = {}
      payload.messageId = messageId

      const requestOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      }

      const url = this.domainOrigin + '/api/chatbot/response'

      fetch(url, requestOptions)
        .then(response => response.json())
        .then(apiObject => {
          try {
            if (apiObject.rc == 0) {
              apiObject.chatbot_reply['timestamp'] = this.getTimestamp()
              this.messages.push(apiObject.chatbot_reply)
              resolve(apiObject.message)
            } else {
              console.log('Failed to get chatbot reply')
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
              apiObject.chatgpt_reply['timestamp'] = this.getTimestamp()
              this.messages.push(apiObject.chatgpt_reply)

              resolve(apiObject.message)
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
