<template>
  <div class="min-h-screen bg-linear-to-br from-green-50 to-teal-100">
    <div class="max-w-6xl mx-auto px-6 py-16">
      <h1 class="text-5xl font-light text-gray-800 mb-10">Les Cours</h1>

      <div class="space-y-8">
        <!-- Au studio de Larchant -->
        <section class="bg-white rounded-lg shadow-sm p-8 space-y-6">
          <h2 class="text-3xl font-light text-gray-900">Au studio de Larchant</h2>

          <div class="space-y-6 text-gray-700">
            <div class="flex items-start gap-4">
              <div class="w-24 h-24 rounded-lg overflow-hidden ring-1 ring-black/5 shrink-0 bg-white p-2">
                <NuxtImg src="/images/pose1.png" alt="Pratique intermédiaire / avancé" class="w-full h-full object-contain" />
              </div>
              <div class="flex-1">
                <div class="flex flex-col sm:flex-row sm:items-baseline sm:justify-between gap-1">
                  <h3 class="text-xl font-medium text-gray-900">Pratique intermédiaire / avancé</h3>
                  <p class="text-sm text-gray-500">* Adaptation aux débutant·es possible</p>
                </div>
                <ul class="mt-2 space-y-1">
                  <li>Lundi — 12h20–13h50</li>
                  <li>Mercredi — 18h30–20h00</li>
                </ul>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <div class="w-24 h-24 rounded-lg overflow-hidden ring-1 ring-black/5 shrink-0 bg-white p-2">
                <NuxtImg src="/images/pose2.png" alt="Yoga doux" class="w-full h-full object-contain" />
              </div>
              <div class="flex-1">
                <h3 class="text-xl font-medium text-gray-900">Yoga doux</h3>
                <ul class="mt-2 space-y-1">
                  <li>Jeudi — 12h20–13h20</li>
                </ul>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <div class="w-24 h-24 rounded-lg overflow-hidden ring-1 ring-black/5 shrink-0 bg-white p-2">
                <NuxtImg src="/images/pose3.png" alt="Pratique débutant / intermédiaire" class="w-full h-full object-contain" />
              </div>
              <div class="flex-1">
                <h3 class="text-xl font-medium text-gray-900">Pratique débutant / intermédiaire</h3>
                <ul class="mt-2 space-y-1">
                  <li>Jeudi — 18h30–20h00</li>
                </ul>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <div class="w-24 h-24 rounded-lg overflow-hidden ring-1 ring-black/5 shrink-0 bg-white p-2">
                <NuxtImg src="/images/pose4.png" alt="Yoga adapté" class="w-full h-full object-contain" />
              </div>
              <div class="flex-1">
                <h3 class="text-xl font-medium text-gray-900">Yoga adapté</h3>
                <ul class="mt-2 space-y-1">
                  <li>Vendredi — 12h00–13h00</li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        <!-- Dans d'autres lieux -->
        <section class="bg-white rounded-lg shadow-sm p-8 space-y-8">
          <h2 class="text-3xl font-light text-gray-900">Dans d'autres lieux</h2>

          <!-- La Chapelle-la-Reine -->
          <div class=" border-gray-100 rounded-lg ">
            <div class="flex items-start gap-4">
              <div class="w-24 h-24 rounded-lg overflow-hidden ring-1 ring-black/5 shrink-0 bg-white p-2">
                <NuxtImg src="/images/pose5.png" alt="La Chapelle-la-Reine" class="w-full h-full object-contain" />
              </div>
              <div class="flex-1">
                <div class="flex flex-col sm:flex-row sm:items-baseline sm:justify-between gap-2">
                  <h3 class="text-2xl font-light text-gray-900">La Chapelle-la-Reine</h3>
                  <span class="text-sm text-teal-700">Débutant / intermédiaire</span>
                </div>
                <ul class="mt-3 space-y-1 text-gray-700">
                  <li>Lundi — 10h45–11h45</li>
                  <li>Mardi — 18h00–19h00</li>
                  <li>Mardi — 19h00–20h00</li>
                  <li>Mardi — 20h00–21h00 (yoga doux)</li>
                </ul>
                <div class="mt-4 text-gray-600">
                  <p class="font-medium">Association DMD</p>
                  <p>Rue du Clos<br />77760 La Chapelle-la-Reine</p>
                </div>
                <div class="mt-4">
                  <UButton to="https://www.assodmd.fr/2023/SiteDMD/menu.php" target="_blank" rel="noopener" color="primary" variant="soft">
                    En savoir plus
                  </UButton>
                </div>
              </div>
            </div>
          </div>

          <!-- Nemours -->
          <div class=" border-gray-100 rounded-lg ">
            <div class="flex items-start gap-4">
              <div class="w-24 h-24 rounded-lg overflow-hidden ring-1 ring-black/5 shrink-0 bg-white p-2">
                <NuxtImg src="/images/pose5.png" alt="Nemours" class="w-full h-full object-contain" />
              </div>
              <div class="flex-1">
                <div class="flex flex-col sm:flex-row sm:items-baseline sm:justify-between gap-2">
                  <h3 class="text-2xl font-light text-gray-900">Nemours</h3>
                  <span class="text-sm text-teal-700">Débutant / intermédiaire</span>
                </div>
                <ul class="mt-3 space-y-1 text-gray-700">
                  <li>Jeudi — 10h00–11h30</li>
                </ul>
                <div class="mt-4 text-gray-600">
                  <p class="font-medium">Magic Form</p>
                  <p>37 avenue Carnot<br />77140 Nemours</p>
                </div>
                <div class="mt-4">
                  <UButton to="https://magic-form.fr/clubs/saint-pierre-les-nemours" target="_blank" rel="noopener" color="primary" variant="soft">
                    En savoir plus
                  </UButton>
                </div>
              </div>
            </div>
          </div>
          
          <!-- Le Vaudoué -->
          <div class=" border-gray-100 rounded-lg">
            <div class="flex items-start gap-4">
              <div class="w-24 h-24 rounded-lg overflow-hidden ring-1 ring-black/5 shrink-0 bg-white p-2">
                <NuxtImg src="/images/pose5.png" alt="Le Vaudoué" class="w-full h-full object-contain" />
              </div>
              <div class="flex-1">
                <div class="flex flex-col sm:flex-row sm:items-baseline sm:justify-between gap-2">
                  <h3 class="text-2xl font-light text-gray-900">Le Vaudoué</h3>
                   <span class="text-sm text-teal-700">Débutant / intermédiaire</span>
                </div>
                <ul class="mt-3 space-y-1 text-gray-700">
                  <li>Lundi — 19h00–20h30</li>
                </ul>
                <div class="mt-4 text-gray-600">
                  <p class="font-medium">ESF77</p>
                </div>
                <div class="mt-4">
                  <UButton to="https://magic-form.fr/clubs/saint-pierre-les-nemours" target="_blank" rel="noopener" color="primary" variant="soft">
                    En savoir plus
                  </UButton>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- À domicile -->
        <section class="bg-white rounded-lg shadow-sm p-8 space-y-4">
          <h2 class="text-3xl font-light text-gray-900">À domicile</h2>
          <ul class="list-disc pl-5 text-gray-700 space-y-1">
            <li>Cours postural — seul·e ou à plusieurs</li>
            <li>Yoga pré et post-natal — pour accompagner votre grossesse</li>
            <li>Pranayama — explorez votre respiration et relâchez votre esprit</li>
          </ul>
          <div class="pt-2">
            <UButton to="mailto:yoga@antoninerochet.fr" color="primary">Me contacter</UButton>
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

useSeoMeta({
  title: 'Les Cours - Antonine Rochet Yoga',
  description: 'Découvrez les cours de yoga Iyengar proposés par Antonine Rochet'
})
</script>
