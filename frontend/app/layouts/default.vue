<template>
    <div class="min-h-screen xl:flex">
        <aside
            class="fixed mt-16 flex flex-col lg:mt-0 top-0 px-5 left-0 bg-white dark:bg-gray-900 dark:border-gray-800 text-gray-900 h-screen transition-all duration-300 ease-in-out z-99999 border-r border-gray-200"
        >
            <div class="py-8 flex lg:justify-center">
                <router-link to="/">
                    Medical
                </router-link>
            </div>
            <div class="flex flex-col overflow-y-auto duration-300 ease-linear no-scrollbar">
                <nav class="mb-6">
                    <div class="flex flex-col gap-4">
                        <div v-for="(menuGroup, groupIndex) in menuGroups" :key="groupIndex">
                            <h2 class="mb-4 text-xs uppercase flex leading-[20px] text-gray-400 lg:justify-center">
                                {{ menuGroup.title }}
                            </h2>
                            <ul class="flex flex-col gap-4">
                                <li v-for="(item, index) in menuGroup.items" :key="index">
                                    <router-link :to="item.path" class="menu-item group">
                                        <span class="menu-item-icon-inactive"
                                        >
                                            {{ item.name }}
                                        </span>
                                    </router-link>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
            </div>
        </aside>
        <div class="flex-1 transition-all duration-300 ease-in-out lg:ml-[160px]">
            <header
                class="sticky top-0 flex w-full bg-white border-gray-200 z-99999 dark:border-gray-800 dark:bg-gray-900 lg:border-b"
            >
                <div class="flex flex-col items-center justify-between grow lg:flex-row lg:px-6">
                    <div
                        class="items-center justify-between w-full gap-4 px-5 py-4 shadow-theme-md lg:flex lg:justify-end lg:px-0 lg:shadow-none flex"
                    >
                        <div class="flex items-center gap-2 2xsm:gap-3"></div>
                        <div class="relative" ref="dropdownRef">
                            <button
                                class="flex items-center text-gray-700 dark:text-gray-400"
                                @click.prevent="toggleDropdown"
                            >
                                <span class="mr-3 overflow-hidden h-11 w-11">
                                    <img src="/images/user.png" alt="User" />
                                </span>

                                <span class="block mr-1 font-medium text-theme-sm">Usuario </span>
                            </button>
                        </div>
                    </div>
                </div>
            </header>
            <div class="p-4 mx-auto max-w-(--breakpoint-2xl) md:p-6">
                <slot></slot>
            </div>
        </div>
    </div>
</template>

<script setup>
const menuGroups = [
  {
    title: "Administración",
    items: [
        {
            name: "Historia Clínica",
            path: "/",
        }
    ],
  }
];
</script>
