<template>
    <section class="pt-1 px-2 flex flex-col">
        <p v-if="!continuedMessage" class="text-slate-gray text-sm px-[48px]"
            :class="{ 'text-right': sender !== 'bot' }">{{ timestamp }}</p>
        <div class="flex gap-x-4"
            :class="{ 'justify-start flex-row-reverse': sender !== 'bot', 'px-[48px]': continuedMessage }">
            <span v-if="!continuedMessage" class="w-8 h-8 bg-black rounded-full"></span>
            <span class="py-1 px-3 rounded-lg max-w-48 sm:max-w-72 font-montserrat text-sm flex items-center"
                :class="{ 'bg-blue-500 text-white': sender !== 'bot', 'bg-slate-200': sender == 'bot' }">{{ message
                }}</span>
        </div>
    </section>
</template>

<script>
export default {
    props: {
        sender: {
            type: String
        },
        message: {
            type: String
        },
        timestamp: {
            type: String
        },
        continuedMessage: {
            type: Boolean,
            default: false
        }
    },

}
</script>

<style scoped></style>