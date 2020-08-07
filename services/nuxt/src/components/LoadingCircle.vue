<template>
  <v-layout flex>
    <v-progress-circular
      class="progress-contain"
      :size="35"
      :width="3"
      color="var(--primary-purple)"
      indeterminate
    >
    </v-progress-circular>
  </v-layout>
</template>

<script>
export default {

}
</script>

<style scoped>
>>>.progress-contain {
  align-self: center;
  margin: 0 auto;
  width: 100%;
  padding-top: 20rem;
}
</style>
