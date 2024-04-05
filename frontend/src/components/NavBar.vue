<template>
    <nav class="max-container py-2 flex justify-between bg-dark-turquoise border-2 border-dark-turquoise">
        <h1 class="text-white ms-4 font-semibold text-2xl">{{ parseFloat(user.multiplier).toFixed(1) }} x</h1>
        <h1 class="text-white ms-4 font-semibold text-2xl hover:cursor-pointer" @click="togglePrizeModal">{{
            user.score }} 🔥</h1>
        <div class="flex gap-x-2 me-2">
            <button class="px-4 border-2 border-red-500 text-white rounded-lg hover:bg-red-500"
                @click="toggleModal">Login</button>
        </div>
    </nav>
</template>

<script>
export default {
    emits: ['toggleModalVisibility', "togglePrizeModalVisibility"],
    props: {
        user: {
            type: Object,
        },
    },
    data() {
        return {
            modalVisibility: false
        }
    },
    methods: {
        toggleModal() {
            this.$emit('toggleModalVisibility')
        },
        togglePrizeModal() {
            this.$emit('togglePrizeModalVisibility')
        }
    },
}
</script>

<style scoped></style>