<template>
  <div class="min-h-screen bg-gradient-to-br from-green-50 to-teal-100">
    <div class="max-w-6xl mx-auto px-6 py-16">
      <h1 class="text-5xl font-light text-gray-800 mb-10">L'Enseignante</h1>

      <div class="flex flex-col lg:flex-row gap-8 mb-10">
        <!-- Image verticale à gauche -->


        <!-- Contenu principal -->
        <div class="flex-1 space-y-8">
          <div class="bg-white rounded-lg shadow-sm p-8">
            <h2 class="text-3xl font-light text-gray-800 mb-6">Antonine Rochet</h2>
            <p class="text-xl text-gray-600 leading-relaxed mb-6">
              Professeure certifiée de yoga Iyengar et accompagnatrice en montagne.
            </p>
          </div>

          <!-- Image 2 en dessous du bloc blanc -->
          <div class="rounded-lg overflow-hidden shadow-lg">
            <NuxtImg src="/images/anto2.jpg" alt="Antonine Rochet" class="w-full h-auto" />
          </div>
        </div>

                <div class="lg:w-80 shrink-0">
          <div class="rounded-lg overflow-hidden shadow-lg sticky top-8">
            <NuxtImg src="/images/anto1.jpg" alt="Antonine Rochet" class="w-full h-auto" />
          </div>
        </div>
      </div>

      
      
      <div class="prose prose-lg max-w-none">

        <h2 class="text-3xl font-light text-gray-800 mt-12 mb-6">Formation</h2>
        <p class="text-gray-600 leading-relaxed mb-4">
          Antonine a découvert le yoga Iyengar il y a plus de 15 ans et s'est formée auprès des 
          meilleurs enseignants en France et en Inde.
        </p>
        <ul class="space-y-2 text-gray-600 mb-6">
          <li class="flex items-start">
            <span class="text-purple-600 mr-2">•</span>
            <span>Certificat d'enseignement du yoga Iyengar</span>
          </li>
          <li class="flex items-start">
            <span class="text-purple-600 mr-2">•</span>
            <span>Formation continue auprès de professeurs seniors</span>
          </li>
  
        </ul>

        <h2 class="text-3xl font-light text-gray-800 mt-12 mb-6">Parcours</h2>
        <p class="text-gray-600 leading-relaxed">
          Passionnée par la montagne et le yoga, Antonine a à cœur de transmettre ces deux pratiques 
          qui se complètent merveilleusement. L'attention, la présence et le respect de son corps 
          développés dans la pratique du yoga sont des qualités essentielles en montagne.
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
  title: 'L\'Enseignante - Antonine Rochet',
  description: 'Découvrez le parcours d\'Antonine Rochet, professeure de yoga Iyengar'
})
</script>
