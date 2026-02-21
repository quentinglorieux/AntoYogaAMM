<template>
  <div class="my-10 overflow-hidden bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-4">
      <h3 class="text-teal-900 text-xl font-light tracking-wide italic">L'album du chantier</h3>
    </div>

    <UScrollArea
      class="w-full h-auto"
      :ui="{
        viewport: 'px-4 sm:px-6 lg:px-8 py-4 no-scrollbar'
      }"
    >
      <div class="flex gap-4 overflow-x-auto snap-x snap-mandatory no-scrollbar pb-4">
        <div 
          v-for="(img, i) in images" 
          :key="i"
          class="flex-none w-[85vw] sm:w-[500px] aspect-4/3 snap-center"
        >
          <div class="relative h-full w-full overflow-hidden rounded-lg group cursor-pointer" @click="openLightbox(i)">
            <NuxtImg 
              :src="img.src" 
              :alt="img.alt || 'Photo du chantier'"
              class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-110"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-6">
              <p class="text-white text-sm italic">{{ img.alt }}</p>
            </div>
          </div>
        </div>
      </div>
    </UScrollArea>

    <!-- Lightbox -->
    <Teleport to="body">
      <div
        v-if="lightboxIndex !== null"
        class="fixed inset-0 z-[100] bg-black/95 flex items-center justify-center p-4"
        @click.self="closeLightbox"
      >
        <button
          class="absolute top-6 right-6 text-white text-4xl leading-none hover:text-gray-300 z-10"
          @click="closeLightbox"
        >✕</button>
        
        <button
          v-if="lightboxIndex > 0"
          class="absolute left-6 text-white text-5xl hover:text-gray-300 z-10 hidden sm:block"
          @click="lightboxIndex--"
        >‹</button>
        
      <div class="relative max-h-screen">
          <NuxtImg
            v-if="activeImage"
            :src="activeImage.src"
            :alt="activeImage.alt || ''"
            class="max-h-[90vh] max-w-[90vw] object-contain rounded shadow-2xl"
          />
          <p v-if="activeImage && activeImage.alt" class="mt-4 text-center text-white/80 text-lg italic px-8">
            {{ activeImage.alt }}
          </p>
        </div>

        <button
          v-if="lightboxIndex < images.length - 1"
          class="absolute right-6 text-white text-5xl hover:text-gray-300 z-10 hidden sm:block"
          @click="lightboxIndex++"
        >›</button>
      </div>
    </Teleport>
  </div>
</template>

<script setup lang="ts">
// On tente un import explicite si l'auto-import échoue dans certains contextes MDC
const UScrollArea = resolveComponent('UScrollArea')
const UButton = resolveComponent('UButton')

interface CarouselImage {
  src: string
  alt?: string
}

const props = defineProps<{
  images: CarouselImage[]
}>()

const lightboxIndex = ref<number | null>(null)

const activeImage = computed(() => {
  if (lightboxIndex.value === null) return null
  return props.images[lightboxIndex.value] || null
})

function openLightbox(i: number) {
  lightboxIndex.value = i
}

function closeLightbox() {
  lightboxIndex.value = null
}

// Add keyboard support for lightbox
onMounted(() => {
  window.addEventListener('keydown', (e) => {
    if (lightboxIndex.value !== null) {
      if (e.key === 'Escape') closeLightbox()
      if (e.key === 'ArrowLeft' && lightboxIndex.value > 0) lightboxIndex.value--
      if (e.key === 'ArrowRight' && lightboxIndex.value < props.images.length - 1) lightboxIndex.value++
    }
  })
})
</script>

<style scoped>
.no-scrollbar::-webkit-scrollbar {
  display: none;
}
.no-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>
