class User {
  constructor (domainOrigin) {
    this.domainOrigin = domainOrigin
    this.score = 0
  }

  updateScore (scoreToAdd) {
    this.score += scoreToAdd
  }
}

export default User
