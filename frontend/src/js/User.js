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
