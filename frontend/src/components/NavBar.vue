<template>
    <nav class="max-container py-2 flex justify-between bg-dark-turquoise">
        <h1 class="text-white ms-4 font-semibold text-2xl">{{ user.score }} 🔥</h1>
        <div class="flex gap-x-2 me-2">
            <button class="border-red-500 border-2 hover:bg-red-500 text-off-white w-24 h-8 rounded-full">Login</button>
            <div @click="signInWithGoogle">
                Continue with google
            </div>
            <button
                class="border-red-500 border-2 hover:bg-red-500 text-off-white w-24 h-8 rounded-full">Register</button>
        </div>
    </nav>
</template>

<script>
import { googleSdkLoaded } from 'vue3-google-login'
export default {
    props: {
        user: {
            type: Object,
        },
    },
    data() {
        return {

        }
    },
    methods: {
        signInWithGoogle() {
            googleSdkLoaded(google => {
                google.accounts.oauth2
                    .initCodeClient({
                        client_id: import.meta.env.VITE_GOOGLE_OAUTH_CLIENT_ID,
                        scope: 'email profile openid',
                        redirect_uri: import.meta.env.VITE_GOOGLE_OAUTH_REDIRECT,
                        callback: response => {
                            console.log(response)
                            if (response.code)
                                this.user.fetchGoogleUserData(response.code)
                        },
                    })
                    .requestCode()
            })

        }
    },
}
</script>

<style scoped></style>