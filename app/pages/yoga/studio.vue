<template>
  <div class="relative min-h-screen bg-stone-50 overflow-hidden">
    <!-- Background Illustrations -->
    <!-- <div class="fixed inset-0 z-0 pointer-events-none">
      <NuxtImg
        src="/images/lulu-chaise-nobg.png"
        alt=""
        class="absolute top-1/2 left-1/2 h-full w-auto object-contain"
        style="opacity: 0.4; filter: grayscale(10%) sepia(5%); mix-blend-mode: multiply; transform: translate(-50%, -50%) rotate(3deg);"
      />
    </div> -->

    <div class="relative z-10 max-w-6xl mx-auto px-6 py-16">
      <h1 class="text-5xl font-light text-stone-950 italic mb-10">Le Studio</h1>

      <!-- Carrousel d'images du Studio -->
      <div class="mb-12 md:mb-16 w-full max-w-2xl mx-auto mt-6 md:mt-8 group">
        <UCarousel
          v-slot="{ item }"
          loop
          :autoplay="{ delay: 3000 }"
          arrows
          dots
          :items="studioImages"
          class="w-full overflow-hidden shadow-lg rounded-2xl bg-stone-100/30"
          :ui="{
            item: 'basis-full',
            container: 'h-[190px] md:h-[300px]'
          }"
        >
          <NuxtImg 
            :src="item" 
            alt="Le studio AntoYoga" 
            class="w-full h-full object-contain p-4 md:p-6 transition-transform duration-1000"
            placeholder
          />
        </UCarousel>
      </div>

      <div class="space-y-10 text-stone-800 leading-relaxed">
        <div class="bg-white shadow-sm rounded-2xl p-8 border border-stone-200/60">
          <p class="text-lg italic text-stone-900">
            Situé au cœur de Larchant, le studio est un espace paisible et chaleureux, dédié à la pratique du yoga Iyengar®. Pour vous accueillir dans les meilleures conditions, il est entièrement équipé : 
            tapis, briques, sangles, couvertures, chaises et cordes murales.
          </p>
        </div>

        <section class="bg-white shadow-sm rounded-2xl p-8 border border-stone-200/60">
          <h2 class="text-3xl font-light text-stone-950 mb-4 mt-0 italic">Un esprit associatif</h2>
          <p>
            Les cours de yoga y sont dispensés par Antonine et portés par l'association Larchant Animation, permettant ainsi de maintenir des tarifs abordables pour le plus grand nombre.
            Cette association, forte de ses nombreux bénévoles et de ses 40 ans d'existence,
            propose également des activités variées, conférences, évènements (trail, vélo, concerts, projections, etc.) ou encore sa
            bibliothèque. Visitez leur site <a href="https://larchantanimation.fr/" target="_blank" class="text-orange-600 hover:text-orange-700 underline">ici</a>.
          </p>
        </section>

        <section>
        <div class="text-center mx-auto mb-8 w-full md:w-auto">
          <h2 class="text-3xl font-light text-stone-950 italic m-0">Horaires des cours au studio</h2>
        </div>
        
        <div class="grid md:grid-cols-2 gap-6">
            <!-- Lundi -->
            <div class="bg-white rounded-2xl shadow-xl shadow-stone-200 p-6 border border-stone-100 border-l-4 border-l-orange-500">
              <h3 class="text-xl font-light text-stone-950 mb-4 italic flex items-center gap-2">
                <span class="w-2 h-2 bg-orange-600 rounded-full"></span> Lundi
              </h3>
              <div class="space-y-6">
                <div class="flex items-center gap-4">
                  <div class="w-10 h-10 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-om-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-stone-900">10h45 – 12h00</p>
                    <p class="text-orange-900/80 italic text-sm">Débutant / Intermédiaire</p>
                  </div>
                </div>
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-equilibre-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-stone-900">12h30 – 14h00</p>
                    <p class="text-orange-900/80 italic text-sm">Intermédiaire / Avancé</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Mardi -->
            <div class="bg-white rounded-2xl shadow-xl shadow-stone-200 p-6 border border-stone-100 border-l-4 border-l-orange-500">
              <h3 class="text-xl font-light text-stone-950 mb-4 italic flex items-center gap-2">
                <span class="w-2 h-2 bg-orange-600 rounded-full"></span> Mardi
              </h3>
              <div class="space-y-6">
                <div class="flex items-center gap-4">
                  <div class="w-10 h-10 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-om-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-stone-900">18h30 – 20h00</p>
                    <p class="text-orange-900/80 italic text-sm">Débutant / Intermédiaire</p>
                  </div>
                </div>
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-brique-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-stone-900">20h00 – 21h00</p>
                    <p class="text-orange-900/80 italic text-sm">Yoga doux</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Mercredi -->
            <div class="bg-white rounded-2xl shadow-xl shadow-stone-200 p-6 border border-stone-100 border-l-4 border-l-orange-500">
              <h3 class="text-xl font-light text-stone-950 mb-4 italic flex items-center gap-2">
                <span class="w-2 h-2 bg-orange-600 rounded-full"></span> Mercredi
              </h3>
              <div class="flex items-center gap-4">
                <div class="w-14 h-14 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative">
                  <NuxtImg src="/images/lulu-equilibre-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                </div>
                <div>
                  <p class="font-medium text-stone-900">18h30 – 20h00</p>
                  <p class="text-orange-900/80 italic text-sm">Intermédiaire / Avancé</p>
                </div>
              </div>
            </div>

            <!-- Jeudi -->
            <div class="bg-white rounded-2xl shadow-xl shadow-stone-200 p-6 border border-stone-100 border-l-4 border-l-orange-500">
              <h3 class="text-xl font-light text-stone-950 mb-4 italic flex items-center gap-2">
                <span class="w-2 h-2 bg-orange-600 rounded-full"></span> Jeudi
              </h3>
              <div class="space-y-6">
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-brique-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-stone-900">12h30 – 13h30</p>
                    <p class="text-orange-900/80 italic text-sm">Yoga doux</p>
                  </div>
                </div>
                <div class="flex items-center gap-4">
                  <div class="w-10 h-10 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative">
                    <NuxtImg src="/images/lulu-om-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                  </div>
                  <div>
                    <p class="font-medium text-stone-900">18h30 – 20h00</p>
                    <p class="text-orange-900/80 italic text-sm">Débutant / Intermédiaire</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Vendredi -->
            <div class="bg-white rounded-2xl shadow-xl shadow-stone-200 p-6 border border-stone-100 border-l-4 border-l-orange-500">
              <h3 class="text-xl font-light text-stone-950 mb-4 italic flex items-center gap-2">
                <span class="w-2 h-2 bg-orange-600 rounded-full"></span> Vendredi
              </h3>
              <div class="flex items-center gap-4">
                <div class="w-14 h-14 shrink-0 bg-stone-50/80 rounded-full flex items-center justify-center relative">
                  <NuxtImg src="/images/lulu-corde-nobg.png" alt="" class="w-full h-full object-contain transform scale-150 relative z-10" />
                </div>
                <div>
                  <p class="font-medium text-stone-900">12h00 – 13h00</p>
                  <p class="text-orange-900/80 italic text-sm">Yoga adapté</p>
                </div>
              </div>
            </div>

            <!-- Lien Cours Extérieurs -->
            <div class="bg-white rounded-2xl shadow-sm p-6 border border-orange-500/30 flex flex-col justify-center items-center text-center">
              <p class="text-stone-950 font-light italic mb-4">Antonine intervient aussi à Nemours et Le Vaudoué.</p>
              <UButton to="/yoga/cours" color="error" variant="outline" size="lg" icon="i-heroicons-calendar">
                Voir tous les cours
              </UButton>
            </div>
          </div>
        </section>

        <section class="bg-white shadow-sm rounded-2xl p-8 border border-stone-200/60">
          <h2 class="text-3xl font-light text-stone-950 mb-4 mt-0 italic">Accès</h2>
          <div class="flex flex-col sm:flex-row gap-8 items-center">
            <div class="flex-1">
              <p class="text-lg mb-2">
                <strong>16 Place des Tilleuls, 77760 Larchant.</strong>
              </p>
              <p class="text-orange-900 mb-4 italic">
                Au cœur du village, vue sur l'église. Entrez sans frapper ! 
              </p>
              <p class="text-stone-600 text-sm">
                Des vestiaires et des sanitaires sont à votre disposition pour vous changer sur place.
              </p>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'default'
})

const studioImages = [
  '/images/studio/studio_cordes2.jpg',
  '/images/studio/studio_casier.jpg',
  '/images/studio/studio_fenetres.jpg',
  '/images/studio/studio_matos.jpg'
]

useSeoMeta({
  title: 'Le Studio de Yoga Iyengar à Larchant | Antonine Rochet',
  description: 'Studio de yoga Iyengar® à Larchant près de Fontainebleau. Cours collectifs et particuliers tous niveaux. Planning des cours à La Chapelle-la-Reine, Nemours et Le Vaudoué. Seine-et-Marne 77.',
  keywords: 'studio yoga Larchant, yoga Iyengar® Fontainebleau, cours yoga Seine-et-Marne, yoga 77, planning cours yoga, yoga Nemours, yoga La Chapelle-la-Reine, studio yoga 77'
})
</script>
