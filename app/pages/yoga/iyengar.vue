<template>
  <div class="min-h-screen bg-gradient-to-br from-teal-50 to-green-50 relative overflow-hidden">

    <!-- Lulu illustration — grande en arrière-plan -->
    <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
      <NuxtImg
        src="/images/lulu-corde-nobg.png"
        alt=""
        class="absolute top-1/2 left-1/2 h-[110%] w-auto object-contain"
        style="opacity: 0.11; filter: grayscale(10%) sepia(10%); mix-blend-mode: multiply; transform: translate(-50%, -50%) rotate(-8deg);"
      />
    </div>

    <div class="max-w-6xl mx-auto px-6 py-16 relative z-10">
      <h1 class="text-5xl font-light text-gray-800 mb-4">Le Yoga Iyengar</h1>

      <!-- Composition lignée de transmission -->
      <div class="mb-4 -mx-6 relative overflow-hidden" style="height: 42vw;">

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

      <div class="space-y-8 text-gray-700 leading-relaxed">
        <p class="text-lg">
          Sangles, chaises, briques, bancs, couvertures, bâtons…<br />
          Les supports introduits par B.K.S. Iyengar pour nous guider vers un asana (posture) exacte ou pratiquer le
          pranayama (respiration) sont multiples.
          Tout comme ses indications laissées en héritage :
        </p>


        <blockquote class="border-l-4 border-teal-300 pl-6 py-2 italic text-gray-600 bg-white/30 rounded-r">
          l'extension du gros orteil, la direction donnée à la peau du mollet, le relâchement de la langue…
        </blockquote>

        <p>
          Selon sa discipline, pas une partie de notre corps ne doit échapper à notre conscience.
        </p>

        <section class="bg-white/40 rounded-2xl p-6 relative overflow-hidden">
          <h2 class="text-3xl font-light text-gray-900 mb-4">La méditation dans l'action</h2>
          <p class="mb-4">
            Des asanas les plus simples (tadasana) aux plus complexes (mandalasana), les multiples actions à effectuer à
            l'unisson avec la respiration permettent de s'abandonner à la pratique du yoga.
          </p>
          <p class="mb-4">
            Ainsi, le mental se résorbe, notre volonté de faire s'efface au profit de notre observation qui scrute
            chaque sensation, chaque transformation interne.
          </p>
          <p>
            Le pranayama vient ancrer cela, redonnant toute leur dimension et leur essentialité à l'inspiration et à
            l'expiration.
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
