<template>
    <div>
        <div class="border-x-2 border-dark-turquoise max-container h-screen flex flex-col">
            <section class="flex flex-col gap-y-1 overflow-y-auto">
                <div v-for="(message, index) in chatbot.messages" :key="index">
                    <Message :sender="message.sender" :message="message.body" :timestamp="message.timestamp"
                        :continuedMessage="checkPreviousSender(index)"></Message>
                </div>
                <div ref="hiddenContent" class="pb-[150px]"></div>
            </section>
            <section class="relative">
                <div class="fixed bottom-0 left-0 right-0 bg-white border-x-2 border-dark-turquoise max-container">
                    <Response :options="responses" @emitResponse="handleUserResponse"></Response>
                </div>
            </section>
        </div>
    </div>
</template>

<script>
import Message from '@/components/Message.vue';
import Response from '@/components/Response.vue';


export default {
    components: {
        Message,
        Response
    },
    props: {
        user: {
            type: Object
        },
        chatbot: {
            type: Object
        },
    },
    data() {
        return {
            responses: []
        }
    },
    methods: {
        checkPreviousSender(index) {
            if (index !== 0) {
                return this.chatbot.messages[index - 1].sender === this.chatbot.messages[index].sender;
            }
        },
        async handleUserResponse(message) {
            await this.chatbot.apiGetReplyFromChatbot(message, this.chatbot.messages[this.chatbot.messages.length - 1]["id"], this.chatbot.messages[this.chatbot.messages.length - 1]["body"])
            this.responses = this.chatbot.messages[this.chatbot.messages.length - 1]["responses"]
            this.user.updateScore(5);
            this.scrollToBottom();
        },
        scrollToBottom() {
            this.$refs.hiddenContent.scrollIntoView({ behavior: 'smooth' });
        }
    },
    async created() {
        await this.chatbot.apiGetReplyFromChatbot(null, null, null);
        this.responses = this.chatbot.messages[this.chatbot.messages.length - 1]["responses"]
    },
}
</script>

<style scoped>
/* Add any custom styling here */
</style>
