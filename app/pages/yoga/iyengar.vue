<template>
  <div class="relative min-h-screen bg-stone-50 overflow-hidden">

    <!-- Background Illustrations -->
    <div class="fixed inset-0 z-0 pointer-events-none">
      <NuxtImg
        src="/images/lulu-corde-nobg.png"
        alt=""
        class="absolute top-1/2 left-1/2 h-[110%] w-auto object-contain"
        style="opacity: 0.4; filter: grayscale(10%) sepia(10%); mix-blend-mode: multiply; transform: translate(-50%, -50%) rotate(-8deg);"
      />
    </div>

    <div class="max-w-6xl mx-auto px-6 py-16 relative z-10">
      <h1 class="text-5xl font-light text-stone-950 mb-0 mt-2 relative z-50">Le Yoga Iyengar</h1>

      <!-- Composition lignée de transmission -->
      <div class="-mt-16 md:-mt-20 lg:-mt-24 mb-4 -mx-6 relative overflow-hidden" style="height: 42vw;">

          <!-- Iyengar — à gauche -->
          <div class="absolute left-0 bottom-0 overflow-hidden z-10 hover:z-40 hover:scale-105 transition-all duration-300"
               style="width: calc(100% / 3); transform: rotate(-4deg); transform-origin: bottom left;">
            <NuxtImg src="/images/iyengar.jpg" alt="B.K.S. Iyengar" class="w-full h-auto" />
          </div>

          <!-- Pisano — au centre, surelevé -->
          <div class="absolute overflow-hidden z-20 hover:z-40 hover:scale-105 transition-all duration-300"
               style="left: calc(100% / 3); width: calc(100% / 3); bottom: 4%;">
            <NuxtImg src="/images/pisano.jpg" alt="Pisano" class="w-full h-auto" />
          </div>

          <!-- Danièle — à droite -->
          <div class="absolute right-0 bottom-0 overflow-hidden z-30 hover:z-40 hover:scale-105 transition-all duration-300"
               style="width: calc(100% / 3); transform: rotate(4deg); transform-origin: bottom right;">
            <NuxtImg src="/images/daniele.jpg" alt="Danièle" class="w-full h-auto" />
          </div>

      </div>

      <div class="space-y-8 text-stone-900 leading-relaxed">
        <div class="bg-white/90 backdrop-blur-sm shadow-sm rounded-2xl p-8 border border-stone-200/60 flex flex-col gap-6">
          <p class="text-lg">
            La pratique posturale, voilà une porte d'entrée sur le chemin du yoga. Elle nous fait chercher l'équilibre entre souplesse et
           résistance, entre effort et aisance, elle nous fait chercher tout court. Plus le corps s'engage dans la pratique, plus il se découvre et se conscientise. Il ne faudrait rien 
           dire de plus pour laisser chacun et chacune libre de sillonner.
          </p>
          <blockquote class="border-l-4 border-orange-500 pl-6 py-4 italic text-stone-800 bg-white/60 rounded-r">
            La direction du coccyx, le placement du regard, le mouvement de la peau, le relâchement de la langue : des actions et des contre-actions d'une infinie subtilité pour trouver
            le centre et s'y reposer. B.K.S Iyengar a apporté sa pierre à l'édifice en enrichissant la pratique posturale de supports et de nombreuses indications qui se sont transmises de mentors à élèves.
            Il a ainsi ouvert la pratique à tous les corps, sans discrimination,
            pour pouvoir transmettre le yoga au plus grand nombre et aussi graduellement que faire se peut.
          </blockquote>
        </div>

        <section class="bg-white/90 backdrop-blur-sm shadow-sm rounded-2xl p-8 border border-stone-200/60 relative overflow-hidden">
          <h2 class="text-3xl font-light text-stone-950 mb-4">La méditation dans l'action</h2>
          <p class="mb-4">
            De mentor à élève, depuis B.K.S Iyengar 
          </p>
          <p class="mb-4">
            bla
          </p>
        </section>

        <div class="mt-12 rounded-2xl overflow-hidden shadow-lg mx-2 sm:mx-40">
          <NuxtImg src="/images/anto_kurmasana.png" alt="Antonine Rochet - Kurmasana" class="w-full h-auto" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'default'
})

useSeoMeta({
  title: 'Qu\'est-ce que le Yoga Iyengar ? | Méthode et Bienfaits',
  description: 'Découvrez la méthode de yoga Iyengar : alignement précis, utilisation d\'accessoires, progression adaptée. Idéal pour débutants et pratiquants expérimentés à Fontainebleau et Larchant.',
  keywords: 'yoga Iyengar méthode, qu\'est-ce que le yoga Iyengar, yoga alignement, yoga avec accessoires, yoga débutant, yoga précis, BKS Iyengar, yoga thérapeutique'
})
</script>
