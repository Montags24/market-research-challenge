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

  apiGetReplyFromChatbot (userReply, messageId) {
    console.log('In apiGetReplyFromChatbot')
    console.log(userReply)
    console.log(messageId)

    if (userReply != '' && userReply != null) {
      this.pushUserReplyToMessages(userReply)
    }

    return new Promise((resolve, reject) => {
      const payload = {}
      if (userReply != '' && userReply != null) {
        payload.user_reply = userReply
        payload.message_id = messageId
      }
      console.log(payload)

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
}

export default Chatbot
