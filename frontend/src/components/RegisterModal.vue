<template>
    <div v-if="registerModalVisible">
        <!-- Modal -->
        <div class="fixed inset-0 flex items-center justify-center ">
            <div
                class="bg-white rounded-lg p-6 w-80 sm:w-96 max-w-full shadow-lg transform transition-all duration-300">
                <!-- Modal Header -->
                <div class="flex justify-between items-center border-b-2 border-gray-200 pb-4">
                    <h2 class="text-2xl font-semibold">Register</h2>
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
                    <form class="px-4">
                        <div class="mb-2 flex gap-x-2">
                            <div>
                                <label class="block text-gray-700 text-sm font-bold mb-2" for="first-name">
                                    First Name
                                </label>
                                <input
                                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                                    :class="firstName ? 'border-green-500' : 'border-red-500'" id="first-name"
                                    type="text" v-model="firstName">
                            </div>
                            <div>
                                <label class="block text-gray-700 text-sm font-bold mb-2" for="last-name">
                                    Last Name
                                </label>
                                <input
                                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                                    :class="lastName ? 'border-green-500' : 'border-red-500'" id="last-name" type="text"
                                    v-model="lastName">
                            </div>
                        </div>
                        <div class="mb-2">
                            <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
                                Email
                            </label>
                            <input
                                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                                :class="!validateEmail(email) ? 'border-red-500' : 'border-green-500'" id="email"
                                type="email" v-model="email">
                        </div>
                        <div class="mb-2">
                            <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
                                Password
                            </label>
                            <div class="flex items-center mb-3 gap-x-1">
                                <input
                                    class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                                    :class="!validatePassword(password) ? 'border-red-500' : 'border-green-500'"
                                    id="password" :type="passwordVisibility ? 'password' : 'text'" v-model="password">
                                <img :src="passwordVisibility ? toggleVisibilityOn : toggleVisibilityOff"
                                    alt="toggle-password-visibility" class="hover:cursor-pointer"
                                    @click="togglePasswordVisibility">
                            </div>
                            <div v-if="!validatePassword(password)" class="text-sm text-red-500">
                                <p>Password must contain:</p>
                                <ul class=" text-xs italic list-disc ps-5">
                                    <li :class="{ 'text-green-500': validateTotalCharacters() }">At least 8 characters
                                    </li>
                                    <li :class="{ 'text-green-500': validateUpperCase() }">One uppercase character</li>
                                    <li :class="{ 'text-green-500': validateLowerCase() }">One lowercase character</li>
                                    <li :class="{ 'text-green-500': validateNumber() }">One number</li>
                                    <li :class="{ 'text-green-500': validateSpecial() }">One special character</li>
                                </ul>
                            </div>
                        </div>
                        <div class="flex items-center justify-center">
                            <button
                                class="bg-blue-500  text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                                type="button" :disabled="buttonDisabled()"
                                :class="!buttonDisabled() ? 'hover:bg-blue-700' : 'opacity-50'">
                                Register
                            </button>
                        </div>
                    </form>
                </div>

                <!-- Additional Information -->
                <div class="mt-6 text-sm text-gray-500">
                    <p>Your privacy matters to us. We never share your personal information. By registering, you agree
                        to
                        our <a href="#" class="text-blue-500 hover:underline">terms of service</a>.
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { toggleVisibilityOn } from '@/assets/svg'
import { toggleVisibilityOff } from '@/assets/svg'

export default {
    emits: ['toggleRegisterModalVisibility'],
    props: {
        registerModalVisible: {
            type: Boolean,
            default: false
        },
        user: {
            type: Object
        }
    },
    data() {
        return {
            firstName: '',
            lastName: '',
            email: '',
            password: '',
            passwordError: '',
            toggleVisibilityOff: toggleVisibilityOff,
            toggleVisibilityOn: toggleVisibilityOn,
            passwordVisibility: false
        };
    },
    methods: {
        togglePasswordVisibility() {
            this.passwordVisibility = !this.passwordVisibility
        },
        toggleModal() {
            this.$emit('toggleRegisterModalVisibility')
        },
        validateEmail() {
            const regex = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;
            return regex.test(this.email);
        },
        validatePassword() {
            const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).{8,}$/;

            if (!passwordRegex.test(this.password)) {
                this.passwordError = "Password must contain at least 8 characters, including at least one uppercase letter, one lowercase letter, one number, and one special character.";
                return false
            } else {
                this.passwordError = '';
                return true
            }
        },
        validateUpperCase() {
            return /[A-Z]/.test(this.password);
        },
        validateLowerCase() {
            return /[a-z]/.test(this.password);
        },
        validateNumber() {
            return /[0-9]/.test(this.password);
        },
        validateSpecial() {
            return /[\W_]/.test(this.password);
        },
        validateTotalCharacters() {
            return this.password.length >= 8;
        },
        buttonDisabled() {
            return !this.firstName || !this.lastName || !this.validateEmail() || !this.validatePassword()
        }
    },
};
</script>

<style>
/* Add your styles here */
</style>
