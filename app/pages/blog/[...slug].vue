<template>
    <div class="py-12 bg-white min-h-screen">
        <article v-if="post" class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="mb-8 text-center">
                <h1 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">{{ post.title }}</h1>
                <p v-if="post.date" class="text-gray-500">{{ new Date(post.date).toLocaleDateString('fr-FR', {
                    year:
                        'numeric', month: 'long', day: 'numeric'
                }) }}</p>
            </div>

            <div v-if="post.image" class="mb-8 rounded-xl overflow-hidden shadow-lg">
                <img :src="post.image" :alt="post.title" class="w-full h-auto object-cover max-h-[500px]" />
            </div>

            <div class="prose prose-lg prose-teal prose-headings:text-teal-700 mx-auto">
                <ContentRenderer :value="post" />
            </div>

            <div class="mt-12 pt-8 border-t border-gray-200">
                <NuxtLink to="/blog" class="text-teal-600 hover:text-teal-800 font-medium flex items-center gap-2">
                    &larr; Retour au blog
                </NuxtLink>
            </div>
        </article>
        <div v-else class="text-center py-12">
            <p>Article non trouvé</p>
            <NuxtLink to="/blog" class="text-teal-600 mt-4 inline-block">Retour au blog</NuxtLink>
        </div>
    </div>
</template>

<script setup lang="ts">
const route = useRoute()
const { data: post } = await useAsyncData(route.path, () => {
    return queryCollection('blog').path(route.path).first()
})

useSeoMeta({
    title: post.value?.title,
    description: post.value?.description,
    ogImage: post.value?.image
})
</script>
