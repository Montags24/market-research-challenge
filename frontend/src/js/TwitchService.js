class TwitchService {
  constructor (nango, user) {
    this.nango = nango
    this.user = user
    this.clientId = import.meta.env.VITE_TWITCH_OAUTH_CLIENT_ID
  }

  async signIn () {
    try {
      const providerConfigKey = await this.createConnection()
      console.log(providerConfigKey)
      await this.fetchAccessToken('test-connection-id', providerConfigKey)
    } catch (err) {
      // Handle authentication error
      console.error('Error:', err.message)
      console.error('Type:', err.type)
    }
  }

  async createConnection () {
    const result = await this.nango.auth('twitch', 'test-connection-id')
    return result.providerConfigKey
  }

  async fetchAccessToken (connectionId, providerConfigKey) {
    const options = {
      method: 'GET',
      headers: { Authorization: `Bearer ${import.meta.env.VITE_NANGO_SECRET_KEY}` }
    }

    try {
      const response = await fetch(
        `https://api.nango.dev/connection/${connectionId}?provider_config_key=${providerConfigKey}`,
        options
      )
      const data = await response.json()
      this.fetchUserData(data.credentials.access_token)
    } catch (err) {
      console.error(err)
    }
  }

  fetchUserData (accessToken) {
    console.log('In fetchUserData')
    return new Promise((resolve, reject) => {
      const url = 'https://api.twitch.tv/helix/users'

      const requestOptions = {
        method: 'GET',
        headers: {
          Authorization: 'Bearer ' + accessToken,
          'Client-ID': this.clientId
        }
      }

      fetch(url, requestOptions)
        .then(response => {
          if (response.status === 200) {
            return response.json()
          } else {
            reject(new Error('Failed to fetch user data'))
          }
        })
        .then(userData => {
          userData = userData.data[0]
          console.log(userData)
          this.user.name = userData.display_name
          this.user.email = userData.email
          this.user.avatar = userData.profile_image_url

          this.user.loggedIn = true
          resolve()
        })
        .catch(error => {
          console.error('Error fetching user data:', error)
          reject(error)
        })
    })
  }
}

export default TwitchService
