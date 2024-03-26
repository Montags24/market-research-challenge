<template>
    <section class="flex flex-col justify-center px-4 pb-4 pt-1 max-container">
        <div class="flex pb-2 overflow-x-auto">
            <div class="flex gap-x-2 pb-2">
                <div v-for="(option, index) in options" :key="index" class="pt-1">
                    <button
                        class="border border-slate-400 rounded-full px-3 text-sm font-montserrat whitespace-nowrap hover:bg-blue-500"
                        @click="selectResponse(option)">{{
                    option
                }}</button>
                </div>
            </div>
        </div>
        <div class="w-full border py-2 px-3 rounded-xl flex justify-between">
            <input type="text" :placeholder="options.length > 0 ? 'Select a response' : 'Enter a message'"
                v-model="message" class="w-full placeholder:text-sm flex items-center focus:outline-none"
                :disabled="options.length">
            <button class="ps-3"><v-icon name="io-send" fill="blue" @click="sendMessage" /></button>
        </div>
    </section>
</template>

<script>

export default {
    emits: ['emitResponse'],
    props: {
        options: {
            type: Array
        },
    },
    data() {
        return {
            message: ""
        }
    },
    methods: {
        selectResponse(text) {
            this.$emit('emitResponse', text)
        },
        sendMessage() {
            this.$emit('emitResponse', this.message)
            this.message = ""
        }
    },
}
</script>

<style scoped></style>