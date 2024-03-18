<template>
    <div>
        {{ sender }}
        {{ message }}
        {{ timestamp }}
    </div>
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
    },

}
</script>

<style scoped></style>