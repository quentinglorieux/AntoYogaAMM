<template>
  <div class="min-h-screen bg-linear-to-br from-green-50 to-teal-100">
    <div class="max-w-6xl mx-auto px-6 py-16">
      <h1 class="text-5xl font-light text-gray-800 mb-10">Le Studio</h1>

      <div class="mb-10 rounded-lg overflow-hidden shadow-lg mx-0">
        <NuxtImg src="/images/studio3.jpeg" alt="Le Studio de yoga Iyengar" class="w-full h-auto" />
      </div>

      <div class="space-y-10 text-gray-600 leading-relaxed">
        <p class="text-lg">
          Le studio de yoga est un espace dédié à la pratique du yoga Iyengar, situé dans un cadre
          paisible et lumineux.
        </p>

        <section>
          <h2 class="text-3xl font-light text-gray-800 mb-4 mt-4">Un espace de pratique</h2>
          <p>
            Le studio est équipé de tout le matériel nécessaire à la pratique du yoga Iyengar :
            briques, sangles, couvertures, chaises et cordes murales.
          </p>
        </section>

        <section>
          <h2 class="text-3xl font-light text-gray-800 mb-6">Horaires des cours au studio</h2>
          
          <div class="bg-white rounded-lg shadow-sm p-6 space-y-6">
            <!-- Lundi -->
            <div class="border-l-4 border-teal-400 pl-4">
              <h3 class="text-2xl font-light text-gray-900 mb-3">Lundi</h3>
              <div class="flex items-start gap-4">
                <div class="w-20 h-20 rounded-lg overflow-hidden ring-1 ring-black/5 shrink-0 bg-white p-2">
                  <NuxtImg src="/images/pose1.png" alt="Pratique intermédiaire / avancé" class="w-full h-full object-contain" />
                </div>
                <div class="flex-1">
                  <p class="text-lg font-medium text-gray-900">12h20–13h50</p>
                  <p class="text-gray-700">Pratique intermédiaire / avancé</p>
                  <p class="text-sm text-gray-500 mt-1">* Adaptation aux débutant·es possible</p>
                </div>
              </div>
            </div>

            <!-- Mercredi -->
            <div class="border-l-4 border-teal-400 pl-4">
              <h3 class="text-2xl font-light text-gray-900 mb-3">Mercredi</h3>
              <div class="flex items-start gap-4">
                <div class="w-20 h-20 rounded-lg overflow-hidden ring-1 ring-black/5 shrink-0 bg-white p-2">
                  <NuxtImg src="/images/pose1.png" alt="Pratique intermédiaire / avancé" class="w-full h-full object-contain" />
                </div>
                <div class="flex-1">
                  <p class="text-lg font-medium text-gray-900">18h30–20h00</p>
                  <p class="text-gray-700">Pratique intermédiaire / avancé</p>
                  <p class="text-sm text-gray-500 mt-1">* Adaptation aux débutant·es possible</p>
                </div>
              </div>
            </div>

            <!-- Jeudi -->
            <div class="border-l-4 border-teal-400 pl-4">
              <h3 class="text-2xl font-light text-gray-900 mb-3">Jeudi</h3>
              <div class="space-y-4">
                <div class="flex items-start gap-4">
                  <div class="w-20 h-20 rounded-lg overflow-hidden ring-1 ring-black/5 shrink-0 bg-white p-2">
                    <NuxtImg src="/images/pose2.png" alt="Yoga doux" class="w-full h-full object-contain" />
                  </div>
                  <div class="flex-1">
                    <p class="text-lg font-medium text-gray-900">12h20–13h20</p>
                    <p class="text-gray-700">Yoga doux</p>
                  </div>
                </div>
                <div class="flex items-start gap-4">
                  <div class="w-20 h-20 rounded-lg overflow-hidden ring-1 ring-black/5 shrink-0 bg-white p-2">
                    <NuxtImg src="/images/pose3.png" alt="Pratique débutant / intermédiaire" class="w-full h-full object-contain" />
                  </div>
                  <div class="flex-1">
                    <p class="text-lg font-medium text-gray-900">18h30–20h00</p>
                    <p class="text-gray-700">Pratique débutant / intermédiaire</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Vendredi -->
            <div class="border-l-4 border-teal-400 pl-4">
              <h3 class="text-2xl font-light text-gray-900 mb-3">Vendredi</h3>
              <div class="flex items-start gap-4">
                <div class="w-20 h-20 rounded-lg overflow-hidden ring-1 ring-black/5 shrink-0 bg-white p-2">
                  <NuxtImg src="/images/pose4.png" alt="Yoga adapté" class="w-full h-full object-contain" />
                </div>
                <div class="flex-1">
                  <p class="text-lg font-medium text-gray-900">12h00–13h00</p>
                  <p class="text-gray-700">Yoga adapté</p>
                </div>
              </div>
            </div>
                      <div class="mt-6">
            <UButton to="/yoga/cours" color="primary" size="lg">
              Voir les autres cours
            </UButton>
          </div>
          </div>
        </section>

        <section>
          <h2 class="text-3xl font-light text-gray-800 mb-4 mt-4">Accès</h2>
          <p class="mb-4">
            Au 16 Place des Tilleuls, 77760 Larchant.<br />
            Entrez sans frapper ! <br />
            Des vestiaires et des sanitaires sont à votre disposition.
          </p>

        </section>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'default'
})

useSeoMeta({
  title: 'Le Studio de Yoga Iyengar à Larchant | Antonine Rochet',
  description: 'Studio de yoga Iyengar à Larchant près de Fontainebleau. Cours collectifs et particuliers tous niveaux. Planning des cours à La Chapelle-la-Reine, Nemours et Le Vaudoué. Seine-et-Marne 77.',
  keywords: 'studio yoga Larchant, yoga Iyengar Fontainebleau, cours yoga Seine-et-Marne, yoga 77, planning cours yoga, yoga Nemours, yoga La Chapelle-la-Reine, studio yoga 77'
})
</script>
