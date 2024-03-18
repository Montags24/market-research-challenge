<template>
    <nav class="max-container py-2 flex justify-between bg-dark-turquoise">
        <h1 class="text-white ms-4 font-semibold text-2xl">{{ user.score }} 🔥</h1>
        <div class="flex gap-x-2 me-2">
            <button class="border-red-500 border-2 hover:bg-red-500 text-off-white w-24 h-8 rounded-full">Login</button>
            <button
                class="border-red-500 border-2 hover:bg-red-500 text-off-white w-24 h-8 rounded-full">Register</button>
        </div>
    </nav>
</template>

<script>
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
}
</script>

<style scoped></style>