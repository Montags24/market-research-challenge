<template>
    <div class="border-x-2 border-dark-turquoise max-container h-screen flex flex-col">
        <!-- SECTION FOR CHAT MESSAGES -->
        <div class="flex flex-col gap-y-1 overflow-y-auto">
            <div v-for="(message, index) in chatbot.messages" :key="index">
                <Message :sender="message.sender" :message="message.body" :timestamp="message.timestamp"
                    :continuedMessage="checkPreviousSender(index)" :user="user"></Message>
            </div>
            <div ref="hiddenContent" class="pb-[150px]"></div>
        </div>
        <!-- SECTION FOR CHAT RESPONSES -->
        <div class="relative">
            <div class="fixed bottom-0 left-0 right-0 bg-white border-x-2 border-dark-turquoise max-container">
                <Response :options="chatbot.responses" @emitResponse="handleUserResponse"></Response>
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
        Response,

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
                return this.chatbot.messages[index - 1].sender === this.chatbot.messages[index].sender;
            }
        },
        async handleUserResponse(userReply) {
            await this.chatbot.handleUserReply(userReply)
            this.scrollToBottom();
        },
        scrollToBottom() {
            // allows for a messaging app user experience where the chat scrolls down
            this.$refs.hiddenContent.scrollIntoView({ behavior: 'smooth' });
        }
    },
    async created() {
        await this.chatbot.apiGetQuestionBank("welcome_question_bank")
        this.chatbot.startWelcomeChat()
    },
}
</script>

<style scoped>
/* Add any custom styling here */
</style>
