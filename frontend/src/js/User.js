class User {
  constructor (domainOrigin) {
    this.domainOrigin = domainOrigin
    this.score = 0
    this.multiplier = 1.0
    this.avatar = 'ri-chat-voice-fill'
    this.name = ''
    this.age = ''
    this.email = ''
    this.gender = ''
    this.loggedIn = false
  }

  updateScore (scoreToAdd) {
    this.score += scoreToAdd
  }

  updateGender (gender) {
    if (gender != '') {
      this.gender = gender
    }
  }

  updateName (name) {
    if (name != '') {
      this.name = name
    }
  }

  updateAge (userReply) {
    if (userReply != '') {
      this.age = userReply
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
