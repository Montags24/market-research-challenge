<template>
    <div v-if="visible">
        <!-- Modal -->
        <div class="fixed inset-0 flex items-center justify-center ">
            <div
                class="bg-white rounded-lg p-6 w-80 sm:w-96 max-w-full shadow-lg transform transition-all duration-300">
                <!-- Modal Header -->
                <div class="flex justify-between items-center border-b-2 border-gray-200 pb-4">
                    <h2 class="text-2xl font-semibold">Login</h2>
                    <button @click="toggleModal" class="text-gray-500 hover:text-gray-700 focus:outline-none">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                            class="feather feather-x">
                            <line x1="18" y1="6" x2="6" y2="18"></line>
                            <line x1="6" y1="6" x2="18" y2="18"></line>
                        </svg>
                    </button>
                </div>

                <!-- Modal Content -->
                <div class="mt-6 space-y-4">
                    <div class="flex flex-col space-y-4">
                        <button
                            class="flex items-center justify-center gap-2 bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition duration-300">
                            <img src="https://svgshare.com/i/14iM.svg" alt="Facebook Icon" class="h-[24px]">
                            Login with Facebook
                        </button>
                        <button
                            class="flex items-center justify-center gap-2 border-slate-200 border-2 bg-white text-gray-800 px-4 py-2 rounded-lg hover:bg-slate-200 transition duration-300"
                            @click="signInWithGoogle">
                            <img src="https://svgshare.com/i/14iL.svg" alt="Google Icon" class="h-[24px]">
                            Login with Google
                        </button>
                        <p class="text-lg text-gray-600">Don't have an account?</p>
                        <button
                            class="flex items-center justify-center gap-2 border-slate-200 border-2 bg-dark-turquoise text-white px-4 py-2 rounded-lg hover:bg-black transition duration-300">
                            Register
                        </button>
                    </div>
                </div>

                <!-- Additional Information -->
                <div class="mt-6 text-sm text-gray-500">
                    <p>Your privacy matters to us. We never share your personal information. By logging in, you agree to
                        our <a href="#" class="text-blue-500 hover:underline">terms of service</a>.
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { googleSdkLoaded } from 'vue3-google-login'
export default {
    emits: ['toggleModalVisibility'],
    props: {
        visible: {
            type: Boolean,
            default: false
        },
        user: {
            type: Object
        }
    },
    data() {
        return {
        };
    },
    methods: {
        toggleModal() {
            this.$emit('toggleModalVisibility')
        },
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
            this.toggleModal()
        },
    },
};
</script>

<style>
/* Add your styles here */
</style>
