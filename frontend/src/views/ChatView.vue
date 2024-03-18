<template>
    <div>
        <div class="border-x-2 border-dark-turquoise max-container h-screen flex flex-col">
            <section class="flex flex-col gap-y-1 overflow-y-auto">
                <div v-for="(message, index) in messages" :key="index">
                    <Message :sender="message.sender" :message="message.body" :timestamp="message.timestamp"
                        :continuedMessage="checkPreviousSender(index)"></Message>
                </div>
                <div ref="hiddenContent" class="pb-[150px]"></div>
            </section>
            <section class="relative">
                <div class="fixed bottom-0 left-0 right-0 bg-white border-x-2 border-dark-turquoise max-container">
                    <Response :options="options" @emitResponse="handleUserResponse"></Response>
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
    },
    data() {
        return {
            messages: [
                {
                    "sender": "bot",
                    "body": "Hi there! 👋",
                    "timestamp": "14:46"
                },
                {
                    "sender": "user",
                    "body": "Hey, how's it going?",
                    "timestamp": "14:47"
                },
                {
                    "sender": "bot",
                    "body": "Great, thanks! What are you up to?",
                    "timestamp": "14:47"
                }
            ],
            options: [
                { "text": "Very unlikely" },
                { "text": "Unlikely" },
                { "text": "Likely" },
                { "text": "Very likely" }
            ]
        }
    },
    methods: {
        checkPreviousSender(index) {
            if (index !== 0) {
                return this.messages[index - 1].sender === this.messages[index].sender;
            }
        },
        handleUserResponse(message) {
            this.messages.push({
                "sender": "user",
                "body": message,
                "timestamp": "14:58"
            });
            this.user.updateScore(5);
            this.scrollToBottom();
        },
        scrollToBottom() {
            this.$refs.hiddenContent.scrollIntoView({ behavior: 'smooth' });
        }
    }
}
</script>

<style scoped>
/* Add any custom styling here */
</style>
