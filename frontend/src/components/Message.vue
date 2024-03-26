<template>
    <section class="pt-1 px-2 flex flex-col">
        <p v-if="!continuedMessage" class="text-slate-gray text-sm px-[48px]"
            :class="{ 'text-right': sender !== 'bot' }">{{ timestamp }}</p>
        <div class="flex gap-x-4"
            :class="{ 'justify-start flex-row-reverse': sender !== 'bot', 'px-[48px]': continuedMessage }">
            <span v-if="!continuedMessage" class="w-8 h-8 rounded-full">
                <img v-if="sender === 'bot'" :src="chatbotAvatar" alt="chatbot-avatar">
                <img v-else-if="user.loggedIn" :src="user.avatar" alt="user-avatar" class="rounded-full">
                <v-icon v-else name="ri-chat-voice-fill" fill="blue" scale="1.5" />
            </span>
            <template v-if="isVideoMessage">
                <video class="max-w-48 sm:max-w-72 rounded-lg" controls :poster="previewImage">
                    <source :src="video" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </template>
            <template v-else>
                <span class="py-1 px-3 rounded-lg max-w-48 sm:max-w-72 font-montserrat text-sm flex items-center"
                    :class="{ 'bg-blue-500 text-white': sender !== 'bot', 'bg-slate-200': sender == 'bot' }">{{ message
                    }}</span>
            </template>
        </div>
    </section>
</template>

<script>
import testVideo from '@/assets/test_video.mp4';
import { chatbotAvatar } from '@/assets/images';
import { previewImage } from '@/assets/images';
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
        },
        user: {
            type: Object,
        }
    },
    data() {
        return {
            video: testVideo,
            chatbotAvatar: chatbotAvatar,
            previewImage: previewImage
        }
    },
    computed: {
        // Check if the message is a video URL
        isVideoMessage() {
            return this.message && this.message.endsWith('.mp4');
        },
        isIcon() {
            return this.message && this.message.endsWith('.icon');
        }
    }
}
</script>

<style scoped></style>