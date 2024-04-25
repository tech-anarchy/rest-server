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
          <RouterLink to="/">
            <p style="font-size:50px">&#127969;</p>
          </RouterLink>
          <RouterLink to="/garden">
            <p style="font-size:50px">&#129716;</p>
          </RouterLink>
          <RouterLink to="/aqua"> 
            <p style="font-size:50px">&#129720;</p>
          </RouterLink>

        </div>
        <div class="menu-right">
          <a href="#" class="text-xl">
            DC
          </a>
        </div>
      </div>
    </div>
  </nav>

  <main class="py-6 px-8 bg-gray-100">
    <RouterView />
  </main>
  
</template>

<script setup>
import { HomeModernIcon } from '@heroicons/vue/24/solid'
</script>