<template>
    <div class="py-12 bg-stone-50 min-h-screen">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-12">
                <h1 class="text-3xl font-light text-black sm:text-4xl">Le Blog</h1>
                <p class="mt-4 text-lg text-black">Articles, conseils et actualités autour du Yoga et de la Montagne
                </p>
            </div>

            <!-- Loading State -->
            <div v-if="status === 'pending'" class="text-center py-12">
                <UIcon name="i-heroicons-arrow-path" class="w-8 h-8 animate-spin mx-auto text-orange-600" />
                <p class="mt-4 text-stone-600">Chargement des articles...</p>
            </div>

            <!-- Error State -->
            <div v-else-if="error" class="text-center py-12 text-red-600">
                Une erreur est survenue lors du chargement des articles.
            </div>

            <!-- Content State -->
            <div v-else-if="articles && articles.length > 0" class="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
                <NuxtLink v-for="article in articles" :key="article.path" :to="article.path"
                    class="group flex flex-col overflow-hidden bg-white rounded-lg shadow-sm hover:shadow-md transition-shadow duration-300">
                    <div class="flex-shrink-0 relative overflow-hidden h-58">
                        <img v-if="article.image"
                            class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                            :src="article.image" :alt="article.title" />
                        <div v-else class="h-full w-full bg-stone-100 flex items-center justify-center text-stone-400">
                            <UIcon name="i-heroicons-photo" class="w-12 h-12" />
                        </div>
                    </div>
                    <div class="flex-1 flex flex-col p-6">
                        <div class="flex-1">
                            <p class="text-sm font-medium text-orange-600 mb-2">
                                <span v-if="article.date">{{ new Date(article.date).toLocaleDateString('fr-FR', {
                                    year:
                                        'numeric', month: 'long', day: 'numeric'
                                }) }}</span>
                            </p>
                            <h3 class="text-xl font-semibold text-black group-hover:text-orange-600 transition-colors">
                                {{ article.title }}
                            </h3>
                            <p class="mt-3 text-base text-black line-clamp-3">
                                {{ article.description }}
                            </p>
                        </div>
                        <div class="mt-6 flex items-center text-orange-600 font-medium group-hover:text-orange-700">
                            Lire la suite <span
                                class="ml-1 transition-transform group-hover:translate-x-1">&rarr;</span>
                        </div>
                    </div>
                </NuxtLink>
            </div>

            <!-- Empty State -->
            <div v-else class="text-center py-12 text-stone-600">
                Aucun article disponible pour le moment.
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
const { data: articles, status, error } = await useAsyncData('blog-articles', () => {
    return queryCollection('blog').order('date', 'DESC').all()
})

useSeoMeta({
    title: 'Le Blog - Antonine Rochet | Yoga & Montagne',
    description: 'Retrouvez tous nos articles sur le yoga, l\'escalade, le trail et la maternité dans la région de Fontainebleau.',
})
</script>
