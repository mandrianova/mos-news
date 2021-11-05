<template>
  <div class="markup">
      <top-bar></top-bar>
      <markup-input></markup-input>
  </div>
</template>

<script>
import TopBar from '../components/TopBar'
import MarkupInput from '../components/MarkupInput.vue'

export default {
    components: {
        TopBar,
        MarkupInput
    }
}
</script>