<template>
    <section
        class="flex flex-col gap-y-1 justify-start max-container bg-off-white border-x-2 border-dark-turquoise h-svh">
        <div v-for="(message, index) in messages" :key="index">
            <Message :sender="message.sender" :message="message.body" :timestamp="message.timestamp"
                :continuedMessage="checkPreviousSender(index)"></Message>
        </div>
    </section>
    <section class="relative">
        <Response></Response>
    </section>
</template>

<script>
import Message from '@/components/Message.vue';
import Response from '@/components/Response.vue';
export default {
    components: {
        Message,
        Response
    },
    data() {
        return {
            messages: [
                {
                    "sender": "bot",
                    "body": "Hi there! 👋",
                    "timestamp": "14:46"
                }
                , {
                    "sender": "user",
                    "body": "Hey, how's it going?",
                    "timestamp": "14:47"
                }, {
                    "sender": "bot",
                    "body": "Great, thanks! What are you up to?",
                    "timestamp": "14:47"
                }, {
                    "sender": "user",
                    "body": "Not much, just wanted to say hi!",
                    "timestamp": "14:47"
                }, {
                    "sender": "user",
                    "body": "Can I ask another question?",
                    "timestamp": "14:47"
                }, {
                    "sender": "bot",
                    "body": "Great, thanks! What are you up to?",
                    "timestamp": "14:47"
                },
                {
                    "sender": "bot",
                    "body": "Great, thanks! What are you up to?",
                    "timestamp": "14:47"
                },
            ]
        }
    },
    methods: {
        checkPreviousSender(index) {
            if (index != 0) {
                return this.messages[index - 1].sender == this.messages[index].sender
            }
        }
    },

}
</script>

<style lang="scss" scoped></style>