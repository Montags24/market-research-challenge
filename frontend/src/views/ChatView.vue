<template>
    <div class="border-x-2 border-dark-turquoise max-container h-screen flex flex-col">
        <!-- SECTION FOR CHAT MESSAGES -->
        <div class="flex flex-col gap-y-1 overflow-y-auto">
            <div v-for="(message, index) in chatbot.messages" :key="index">
                <Message :sender="message.sender" :message="message.body" :timestamp="message.timestamp"
                    :continuedMessage="checkPreviousSender(index)"></Message>
            </div>
            <div ref="hiddenContent" class="pb-[150px]"></div>
        </div>
        <!-- SECTION FOR CHAT RESPONSES -->
        <div class="relative">
            <div class="fixed bottom-0 left-0 right-0 bg-white border-x-2 border-dark-turquoise max-container">
                <Response :options="responses" @emitResponse="handleUserResponse"></Response>
            </div>
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
        sleep(time) {
            return new Promise((resolve) => setTimeout(resolve, time));
        },
        async getNextMessageFromChatbot(messageId) {
            await this.sleep(1500)
            await this.chatbot.apiGetNextResponseFromChatbot(messageId)
            this.responses = this.chatbot.messages[this.chatbot.messages.length - 1]["responses"]
            // If no available responses for the user, get next message
            if (!this.chatbot.messages[this.chatbot.messages.length - 1]["response_required"]) {
                this.getNextMessageFromChatbot(this.chatbot.messages[this.chatbot.messages.length - 1]["id"])
                this.scrollToBottom();
            }
            // else wait for user to respond
        },
        async handleUserResponse(userReply) {
            const latestMessageId = this.chatbot.messages[this.chatbot.messages.length - 1]["id"]
            const methodName = this.chatbot.messages[this.chatbot.messages.length - 1]["function"]
            const chatgptReply = this.chatbot.messages[this.chatbot.messages.length - 1]["chatgpt_reply"]

            if (methodName != null) {
                this.user.invokeMethod(methodName, userReply)
            }
            if (chatgptReply) {
                await this.chatbot.apiGetChatGptResponse(userReply, this.chatbot.messages[this.chatbot.messages.length - 1]["body"], this.user.name)
            } else {
                this.chatbot.pushUserReplyToMessages(userReply)
            }

            this.user.updateScore(5);
            this.getNextMessageFromChatbot(latestMessageId)
            this.scrollToBottom();
        },
        scrollToBottom() {
            // allows for a messaging app user experience where the chat scrolls down
            this.$refs.hiddenContent.scrollIntoView({ behavior: 'smooth' });
        }
    },
    async created() {
        // We use -1 here to get message index 0 initially
        await this.chatbot.apiGetNextResponseFromChatbot(-1);
        this.responses = this.chatbot.messages[this.chatbot.messages.length - 1]["responses"]
        if (!this.chatbot.messages[this.chatbot.messages.length - 1]["response_required"]) {
            const latestMessageId = this.chatbot.messages[this.chatbot.messages.length - 1]["id"]
            await this.getNextMessageFromChatbot(latestMessageId)
        }
    },
}
</script>

<style scoped>
/* Add any custom styling here */
</style>
