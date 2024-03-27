class User {
  constructor (domainOrigin) {
    this.domainOrigin = domainOrigin
    this.score = 0
    this.avatar = 'ri-chat-voice-fill'
    this.name = ''
    this.email = ''
    this.gender = 'none'
    this.loggedIn = false
  }

  updateScore (scoreToAdd) {
    this.score += scoreToAdd
  }

  updateGender (userReply) {
    if (userReply === 'male') {
      this.gender = 'male'
    } else if (userReply === 'female') {
      this.gender = 'female'
    }
  }

  updateName (userReply) {
    if (userReply != '') {
      this.name = userReply
    }
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
