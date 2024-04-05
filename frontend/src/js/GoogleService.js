class GoogleService {
  constructor (domainOrigin, user) {
    this.domainOrigin = domainOrigin
    this.user = user
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
              console.log(apiObject.user_data)
              this.user.name = apiObject.user_data.name
              this.user.avatar = apiObject.user_data.picture
              this.user.loggedIn = true
              resolve(apiObject.message)
            } else {
              reject(apiObject.message)
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

export default GoogleService
