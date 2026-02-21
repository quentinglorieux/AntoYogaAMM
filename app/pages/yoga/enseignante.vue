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
              Professeure certifiée de yoga Iyengar et accompagnatrice en montagne.
            </p>
          </div>

          <!-- Image 2 en dessous du bloc blanc -->
          <div class="rounded-lg overflow-hidden shadow-lg">
            <NuxtImg src="/images/anto_soleil.jpeg" alt="Antonine Rochet" class="w-full h-auto" />
          </div>
        </div>

                <div class="lg:w-80 shrink-0">
          <div class="rounded-lg overflow-hidden shadow-lg sticky top-8">
            <NuxtImg src="/images/anto1.jpg" alt="Antonine Rochet" class="w-full h-auto" />
          </div>
        </div>
      </div>

      
      
      <div class="bg-white/90 backdrop-blur-sm shadow-sm rounded-2xl p-8 border border-stone-200/60 prose prose-lg max-w-none">

        <h2 class="text-3xl font-light text-stone-950 mt-12 mb-6">Formation</h2>
        <p class="text-stone-800 leading-relaxed mb-4">
          Antonine a découvert le yoga Iyengar il y a plus de 15 ans et s'est formée auprès des 
          meilleurs enseignants en France et en Inde.
        </p>
        <ul class="space-y-2 text-stone-800 mb-6">
          <li class="flex items-start">
            <span class="text-orange-600 mr-2">•</span>
            <span>Certificat d'enseignement du yoga Iyengar</span>
          </li>
          <li class="flex items-start">
            <span class="text-orange-600 mr-2">•</span>
            <span>Formation continue auprès de professeurs seniors</span>
          </li>
  
        </ul>

        <h2 class="text-3xl font-light text-stone-950 mt-12 mb-6">Parcours</h2>
        <p class="text-stone-800 leading-relaxed">
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
  title: 'Antonine Rochet - Professeure de Yoga Iyengar Certifiée | Fontainebleau',
  description: 'Antonine Rochet, professeure de yoga Iyengar certifiée et accompagnatrice en montagne diplômée. Formation, expérience et approche pédagogique à Larchant et Fontainebleau.',
  keywords: 'Antonine Rochet yoga, professeur yoga Iyengar Fontainebleau, enseignante yoga certifiée, prof yoga Larchant, yoga teacher 77, accompagnatrice montagne yoga'
})
</script>
