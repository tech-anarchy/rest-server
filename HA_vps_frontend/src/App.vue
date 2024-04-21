<template>
  <nav class="py-10 px-8 border-b border-gray-200">
    <div class="max-w-7xl mx-auto">
      <div class="flex items-center justify-between">
        <div class="menu-left">
          <a href="#" class="text-xl">
            RK
          </a>
        </div>
        <div class="menu-center flex space-x-12">
          <a href="#">
            <HomeModernIcon class="h-6 w-6 text-gray-400" />
          </a>
          <a href="#">
            <ArchiveBoxXMarkIcon class="h-6 w-6 text-emerald-500" />
          </a>
          <a href="#">
            <BeakerIcon class="h-6 w-6 text-blue-500" />
          </a>

        </div>
        <div class="menu-right">
          <a href="#" class="text-xl">
            DC
          </a>
        </div>
      </div>
    </div>
  </nav>
  <RouterView />
</template>

<script setup>
import { BeakerIcon, HomeModernIcon } from '@heroicons/vue/24/solid'
import { ArchiveBoxXMarkIcon } from '@heroicons/vue/24/outline'
</script>