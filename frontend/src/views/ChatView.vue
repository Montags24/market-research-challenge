<template>
    <section class="flex flex-col gap-y-1 justify-start max-container">
        <div v-for="(message, index) in messages" :key="index">
            <Message :sender="message.sender" :message="message.body" :timestamp="message.timestamp"></Message>
        </div>
    </section>
    <section>
        <!-- Chat app messages sectuib -->
    </section>
</template>

<script>
import Message from '@/components/Message.vue';
export default {
    components: {
        Message,
    },
    data() {
        return {
            messages: [
                {
                    "sender": "bot",
                    "body": "Hi there!",
                    "timestamp": "14:46"
                }
                , {
                    "sender": "user",
                    "body": "Hey, how's it going?",
                    "timestamp": "14:47"
                }]
        }
    },

}
</script>

<style lang="scss" scoped></style>