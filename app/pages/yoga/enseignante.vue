<template>
  <div class="relative min-h-screen bg-stone-50 overflow-hidden">

    <!-- Background Illustrations -->
    <div class="fixed inset-0 z-0 pointer-events-none">
      <NuxtImg
        src="/images/lulu-om-nobg.png"
        alt=""
        class="absolute top-1/2 left-1/2 h-[110%] w-auto object-contain"
        style="opacity: 0.4; filter: grayscale(10%) sepia(10%); mix-blend-mode: multiply; transform: translate(-50%, -50%) rotate(15deg);"
      />
    </div>

    <div class="max-w-6xl mx-auto px-6 py-16 relative z-10">
      <h1 class="text-5xl font-light text-stone-950 mb-10">L'Enseignante</h1>

      <div class="flex flex-col lg:flex-row gap-8 mb-10">
        <!-- Image verticale à gauche -->


        <!-- Contenu principal -->
        <div class="flex-1 space-y-8">
          <div class="bg-white shadow-sm rounded-2xl p-6 border border-stone-200/60">
            <h2 class="text-3xl font-light text-stone-950 mb-6">Antonine Rochet</h2>
            <p class="text-xl text-stone-800 leading-relaxed mb-6">
              Professeure certifiée de Yoga Iyengar® Niveau 1
            </p>
          </div>

          <!-- Image 2 en dessous du bloc blanc -->
          <div class="rounded-lg overflow-hidden shadow-lg">
            <NuxtImg src="/images/anto_soleil.jpeg" alt="Antonine Rochet" class="w-full h-auto" />
          </div>
        </div>

                <div class="lg:w-80 shrink-0">
          <div class="rounded-lg overflow-hidden shadow-lg sticky top-8">
            <NuxtImg src="/images/studio/anto_equi.png" alt="Antonine Rochet" class="w-full h-auto" />
          </div>
        </div>
      </div>

      
      
      <div class="bg-white/50 backdrop-blur-sm shadow-sm rounded-2xl p-8 border border-stone-200/60 prose prose-lg max-w-none">

        <h2 class="text-3xl font-light text-stone-950 mt-12 mb-6">Parcours</h2>
        <p class="text-stone-800 leading-relaxed mb-4">
          Antonine a découvert le yoga Iyengar® en 2016. Danseuse classique depuis ses 5 ans,
          elle se passionne dès ses premiers cours de yoga Iyengar® pour la 
          précision des alignements et la rigueur de cette pratique. 
          L'amenant d'une discipline de la représentation vers une pratique de l'écoute des ressentis, le yoga la transforme
          et la libère. Elle continue aujourd'hui sur la voie du yoga, continuant à se questionner et à vagabonder dans une pratique
          riche de trésors.
        </p>
        <h2 class="text-3xl font-light text-stone-950 mt-12 mb-6">Formation</h2>
        <ul class="space-y-2 text-stone-800 mb-6">
          <li class="flex items-start">
            <span class="text-orange-600 mr-2">•</span>
            <span>2016-2024 : Élève de Daniele Navelo</span>
          </li>
          <li class="flex items-start">
            <span class="text-orange-600 mr-2">•</span>
            <span>2022 : Obtention du Certificat de Yoga Pré/Post-natal de la Méthode De Gasquet</span>
          </li>
          <li class="flex items-start">
            <span class="text-orange-600 mr-2">•</span>
            <span>2024 : Obtention du Certificat de Yoga Iyengar® Niveau 1</span>
          </li>
          <li class="flex items-start">
            <span class="text-orange-600 mr-2">•</span>
            <span>2024 à aujourd'hui : Élève de Noa Marchand</span>
          </li>
          <li class="flex items-start">
            <span class="text-orange-600 mr-2">•</span>
            <span>A suivi des stages avec : Lydie Drivière, David Meloni, Christian Pisano et Daniele Navelo</span>
          </li>
        </ul>

        <h2 class="text-3xl font-light text-stone-950 mt-12 mb-6">Note</h2>
        <p class="text-stone-800 leading-relaxed">
          Que tout ne fasse plus qu'un. Comment apprendre du yoga pour vivre mieux au quotidien, faire
          face à ses limites et embrasser sa nudité, puiser sa force dans de nouveaux espaces découverts, se reposer dans d'autres,
          laisser monter à ébullition ce qui est parfois caché, 
          s'abandonner avec confiance, se lancer à corps perdu dans les luttes internes et externes et rester enraciné.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'default'
})

useSeoMeta({
  title: 'Antonine Rochet - Professeure de Yoga Iyengar Certifiée | Fontainebleau',
  description: 'Antonine Rochet, professeure de yoga Iyengar® certifiée et accompagnatrice en montagne diplômée. Formation, expérience et approche pédagogique à Larchant et Fontainebleau.',
  keywords: 'Antonine Rochet yoga, professeur yoga Iyengar® Fontainebleau, enseignante yoga certifiée, prof yoga Larchant, yoga teacher 77, accompagnatrice montagne yoga'
})
</script>
