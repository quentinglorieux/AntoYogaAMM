<template>
  <div class="min-h-screen bg-gradient-to-br from-teal-50 to-green-50 relative overflow-hidden">


    <div class="max-w-6xl mx-auto px-6 py-16 relative z-10">
      <h1 class="text-5xl font-light text-gray-800 mb-10">Le Yoga Iyengar</h1>

      <div class="mb-10 rounded-2xl overflow-hidden shadow-lg sm:mx-40 mx-2">
        <NuxtImg src="/images/iyengar.jpg" alt="B.K.S. Iyengar" class="w-full h-auto" />
      </div>

      <div class="space-y-8 text-gray-700 leading-relaxed">
        <p class="text-lg">
          Sangles, chaises, briques, bancs, couvertures, bâtons…<br />
          Les supports introduits par B.K.S. Iyengar pour nous guider vers un asana (posture) exacte ou pratiquer le
          pranayama (respiration) sont multiples.
          Tout comme ses indications laissées en héritage :
        </p>


        <blockquote class="border-l-4 border-teal-300 pl-6 py-2 italic text-gray-600 bg-white/50 rounded-r">
          l'extension du gros orteil, la direction donnée à la peau du mollet, le relâchement de la langue…
        </blockquote>

        <p>
          Selon sa discipline, pas une partie de notre corps ne doit échapper à notre conscience.
        </p>

        <section class="bg-white/70 backdrop-blur-sm rounded-2xl p-8 relative overflow-hidden">
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
          <NuxtImg src="/images/anto5.jpg" alt="Antonine Rochet pratiquant le yoga" class="w-full h-auto grayscale" />
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
