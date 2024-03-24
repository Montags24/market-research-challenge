<template>
    <nav class="max-container py-2 flex justify-between bg-dark-turquoise">
        <h1 class="text-white ms-4 font-semibold text-2xl">{{ user.score }} 🔥</h1>
        <div class="flex gap-x-2 me-2">
            <button
                class="px-3 py-1 border flex gap-2 bg-white border-slate-200 dark:border-slate-700 rounded-lg text-slate-700 dark:text-slate-200 hover:border-slate-400 dark:hover:border-slate-500 hover:text-slate-900 dark:hover:text-slate-300 hover:shadow transition duration-150"
                @click="signInWithGoogle">
                <img class="w-6 h-6" src="https://www.svgrepo.com/show/475656/google-color.svg" loading="lazy"
                    alt="google logo">
                <span>Login <span class="max-sm:hidden">with Google</span></span>
            </button>
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