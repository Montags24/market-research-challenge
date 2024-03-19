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
                    <Response :options="chatbot.messages[chatbot.messages.length - 1]"
                        @emitResponse="handleUserResponse"></Response>
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
        }
    },
    methods: {
        checkPreviousSender(index) {
            if (index !== 0) {
                return this.messages[index - 1].sender === this.messages[index].sender;
            }
        },
        handleUserResponse(message) {
            this.chatbot.apiGetReplyFromChatbot(message, this.chatbot.messages[this.chatbot.messages.length - 1]["id"])
            this.user.updateScore(5);
            this.scrollToBottom();
        },
        scrollToBottom() {
            this.$refs.hiddenContent.scrollIntoView({ behavior: 'smooth' });
        }
    },
    async created() {
        await this.chatbot.apiGetReplyFromChatbot();
    },
}
</script>

<style scoped>
/* Add any custom styling here */
</style>
