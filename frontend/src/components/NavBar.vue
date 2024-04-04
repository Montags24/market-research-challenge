<template>
    <nav class="max-container py-2 flex justify-between bg-dark-turquoise border-2 border-dark-turquoise">
        <h1 class="text-white ms-4 font-semibold text-2xl">{{ parseFloat(user.multiplier).toFixed(1) }} x</h1>
        <h1 class="text-white ms-4 font-semibold text-2xl">{{ user.score }} 🔥</h1>
        <div class="flex gap-x-2 me-2">
            <button class="px-4 border-2 border-red-500 text-white rounded-lg hover:bg-red-500"
                @click="toggleModal">Login</button>
        </div>
    </nav>
</template>

<script>
export default {
    emits: ['toggleModalVisibility'],
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
        toggleModal() {
            this.$emit('toggleModalVisibility')
        }
    },
}
</script>

<style scoped></style>