<template>
  <div class="my-8 grid gap-3" :class="gridClass">
    <div
      v-for="(img, i) in images"
      :key="i"
      class="overflow-hidden rounded-xl shadow-md group cursor-pointer"
      :class="img.wide ? 'col-span-2' : ''"
      @click="openLightbox(i)"
    >
      <NuxtImg
        :src="img.src"
        :alt="img.alt || ''"
        class="w-full h-56 object-cover transition-transform duration-500 group-hover:scale-105"
        :class="img.tall ? 'h-72' : 'h-56'"
      />
    </div>
  </div>

  <!-- Lightbox -->
  <Teleport to="body">
    <div
      v-if="lightboxIndex !== null"
      class="fixed inset-0 z-50 bg-black/90 flex items-center justify-center p-4"
      @click.self="closeLightbox"
    >
      <button
        class="absolute top-4 right-4 text-white text-3xl leading-none hover:text-gray-300"
        @click="closeLightbox"
      >✕</button>
      <button
        v-if="lightboxIndex > 0"
        class="absolute left-4 text-white text-4xl hover:text-gray-300"
        @click="lightboxIndex--"
      >‹</button>
      <NuxtImg
        v-if="activeImage"
        :src="activeImage.src"
        :alt="activeImage.alt || ''"
        class="max-h-[90vh] max-w-[90vw] object-contain rounded-lg shadow-2xl"
      />
      <button
        v-if="lightboxIndex! < images.length - 1"
        class="absolute right-4 text-white text-4xl hover:text-gray-300"
        @click="lightboxIndex!++"
      >›</button>
      <p v-if="activeImage && activeImage.alt" class="absolute bottom-6 left-0 right-0 text-center text-white/70 text-sm px-8">
        {{ activeImage.alt }}
      </p>
    </div>
  </Teleport>
</template>

<script setup lang="ts">
interface GalleryImage {
  src: string
  alt?: string
  wide?: boolean
  tall?: boolean
}

const props = defineProps<{
  images: GalleryImage[]
  columns?: number
}>()

const lightboxIndex = ref<number | null>(null)

const activeImage = computed(() => {
  if (lightboxIndex.value === null) return null
  return props.images[lightboxIndex.value] || null
})

const gridClass = computed(() => {
  const cols = props.columns || (props.images.length >= 3 ? 3 : props.images.length)
  return {
    'grid-cols-1': cols === 1,
    'grid-cols-2': cols === 2,
    'grid-cols-3': cols === 3,
  }
})

function openLightbox(i: number) {
  lightboxIndex.value = i
}
function closeLightbox() {
  lightboxIndex.value = null
}
</script>
