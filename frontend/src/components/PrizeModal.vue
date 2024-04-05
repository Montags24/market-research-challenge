<template>
    <div v-if="visible">
        <!-- Modal -->
        <div class="fixed inset-0 flex items-center justify-center ">
            <div
                class="bg-white rounded-lg p-6 w-80 sm:w-96 max-w-full shadow-lg transform transition-all duration-300">
                <!-- Modal Header -->
                <div class="flex justify-between items-center border-b-2 border-gray-200 pb-4">
                    <h2 class="text-2xl font-semibold">Rewards</h2>
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
                        <div v-for="(prize, index) in prizes" :key="index">
                            <div class="group relative py-1 flex justify-center hover:cursor-pointer">
                                <div
                                    class="absolute -inset-1 bg-gradient-to-r from-purple-600 to-pink-600 rounded-lg blur opacity-25 group-hover:opacity-100 transition duration-500 group-hover:duration-200">
                                </div>
                                <div
                                    class="relative px-2 py-3 bg-white ring-1 ring-gray-900/5 rounded-lg leading-none flex items-center justify-between space-x-4 w-full">
                                    <!-- Added w-full class -->
                                    <img :src="prize.image" alt="" class="h-8">
                                    <p class="text-slate-800 font-montserrat font-semibold text-center">{{ prize.name }}
                                    </p>
                                    <p class="text-slate-800 font-montserrat font-semibold text-center w-15">{{
                                        prize.cost
                                    }}🔥</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import prizes from './index';
export default {

    emits: ['toggleModalVisibility'],
    props: {
        visible: {
            type: Boolean,
            default: false
        },
        user: {
            type: Object
        },
    },
    data() {
        return {
            prizes: prizes
        };
    },
    methods: {
        toggleModal() {
            this.$emit('toggleModalVisibility')
        },
        toggleRegisterModal() {
            this.$emit('toggleRegisterModal')
        },
    },
};
</script>

<style>
/* Add your styles here */
</style>
