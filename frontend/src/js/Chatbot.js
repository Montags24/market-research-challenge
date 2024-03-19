class Chatbot {
  constructor (domainOrigin) {
    this.domainOrigin = domainOrigin
    this.messages = []
  }

  apiGetReplyFromChatbot (userReply, messageId) {
    console.log('In apiGetReplyFromChatbot')

    this.messages.push({
      sender: 'user',
      body: userReply,
      timestamp: '14:58'
    })

    return new Promise((resolve, reject) => {
      const payload = {}
      if (userReply != '' && userReply != null) {
        payload.user_reply = userReply
        payload.message_id = messageId
      }

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
