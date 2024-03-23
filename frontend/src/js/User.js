class User {
  constructor (domainOrigin) {
    this.domainOrigin = domainOrigin
    this.score = 0
    this.avatar = 'ri-chat-voice-fill'
    this.name = ''
    this.gender = 'none'
  }

  updateScore (scoreToAdd) {
    this.score += scoreToAdd
  }

  updateGender (userReply) {
    if (userReply === 'male') {
      this.gender = 'male'
      this.avatar = 'fc-businessman'
    } else if (userReply === 'female') {
      this.gender = 'female'
      this.avatar = 'fc-businesswoman'
    }
  }

  updateName (userReply) {
    if (userReply != '') {
      this.name = userReply
    }
  }

  fetchGoogleUserData (code) {
    console.log('In fetchGoogleUserData')
    return new Promise((resolve, reject) => {
      const payload = {}
      payload.code = code

      const requestOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      }

      const url = this.domainOrigin + '/auth/google/callback'

      fetch(url, requestOptions)
        .then(response => response.json())
        .then(apiObject => {
          try {
            if (apiObject.rc == 0) {
              resolve(apiObject.message)
            } else {
              console.log('Failed to get user details')
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

  invokeMethod (methodName, ...args) {
    // Check if the method exists
    if (typeof this[methodName] === 'function') {
      // Invoke the method
      this[methodName](...args)
    } else {
      console.error(`Method ${methodName} does not exist.`)
    }
  }
}

export default User
