<template lang="pug">
Viewport
  BlockPage
    BlockLine(align="center")
      InlineHeading(:level="1") SpanCharm-Vue
  BlockPage
    BlockLine(align="left")
      InlineHeading(:level="2") Heading
    BlockLine(align="center")
      FilterPopup(:enabled="isPopup", :value="popupText")
        FilterShake(:enabled="isShake", :forever="shakeForever")
          InlineHeading(
            :level="headingLevel",
            :style="{ color: `${color}`, 'background-color': `${bgColor}` }"
          ) {{ text }}
    BlockLine(align="left")
      InlineText Value:
      InlineInput(v-model="text")
    BlockLine(align="left")
      InlineText Level:
      InlineNumber(v-model="headingLevel")
    BlockLine(align="left")
      InlineCheck(
        :default="false",
        yes="Enable Popup",
        no="Disable Popup",
        v-model="isPopup"
      )
    BlockLine(align="left", v-if="isPopup")
      InlineText Popup Text:
      InlineInput(v-model="popupText")
    BlockLine(align="left")
      InlineCheck(
        :default="false",
        yes="Enable Shake",
        no="Disable Shake",
        v-model="isShake"
      )
      InlineCheck(
        v-if="isShake",
        :default="false",
        yes="Shake Forever",
        no="Shake for Mouse",
        v-model="shakeForever"
      )
    BlockLine(align="left")
      InlineText Text RGB:
      InlineInput(type="color", v-model="color")
      InlineText Background RGB:
      InlineInput(type="color", v-model="bgColor")
  BlockPage
    BlockLine(align="left")
      InlineHeading(:level="2") Text
    BlockLine(align="center")
      FilterPopup(:enabled="isPopup", :value="popupText")
        FilterShake(:enabled="isShake", :forever="shakeForever")
          InlineText(
            :style="{ color: `${color}`, 'background-color': `${bgColor}` }"
          ) {{ text }}
    BlockLine(align="left")
      InlineText Value:
      InlineInput(v-model="text")
    BlockLine(align="left")
      InlineCheck(
        :default="false",
        yes="Enable Popup",
        no="Disable Popup",
        v-model="isPopup"
      )
    BlockLine(align="left", v-if="isPopup")
      InlineText Popup Text:
      InlineInput(v-model="popupText")
    BlockLine(align="left")
      InlineCheck(
        :default="false",
        yes="Enable Shake",
        no="Disable Shake",
        v-model="isShake"
      )
      InlineCheck(
        v-if="isShake",
        :default="false",
        yes="Shake Forever",
        no="Shake for Mouse",
        v-model="shakeForever"
      )
    BlockLine(align="left")
      InlineText Text RGB:
      InlineInput(type="color", v-model="color")
      InlineText Background RGB:
      InlineInput(type="color", v-model="bgColor")
  BlockPage
    BlockLine(align="left")
      InlineHeading(:level="2") Button
    BlockLine(align="center")
      FilterPopup(:enabled="isPopup", :value="popupText")
        FilterShake(:enabled="isShake", :forever="shakeForever")
          InlineButton(
            :style="{ color: `${color}`, 'background-color': `${bgColor}` }"
          ) {{ text }}
    BlockLine(align="left")
      InlineText Value:
      InlineInput(v-model="text")
    BlockLine(align="left")
      InlineCheck(
        :default="false",
        yes="Disabled",
        no="Enabled",
        v-model="isDisabled"
      )
    BlockLine(align="left")
      InlineCheck(
        :default="false",
        yes="Enable Popup",
        no="Disable Popup",
        v-model="isPopup"
      )
    BlockLine(align="left", v-if="isPopup")
      InlineText Popup Text:
      InlineInput(v-model="popupText")
    BlockLine(align="left")
      InlineCheck(
        :default="false",
        yes="Enable Shake",
        no="Disable Shake",
        v-model="isShake"
      )
      InlineCheck(
        v-if="isShake",
        :default="false",
        yes="Shake Forever",
        no="Shake for Mouse",
        v-model="shakeForever"
      )
    BlockLine(align="left")
      InlineText Text RGB:
      InlineInput(type="color", v-model="color")
      InlineText Background RGB:
      InlineInput(type="color", v-model="bgColor")
  BlockPage
    BlockLine(align="left")
      InlineHeading(:level="2") Progress
    BlockLine(align="center")
      FilterPopup(:enabled="isPopup", :value="popupText")
        FilterShake(:enabled="isShake", :forever="shakeForever")
          InlineProgress(
            :value="3",
            :max="5",
            :width="100",
            color="red",
            bg-color="cyan"
          )
    BlockLine(align="left")
      InlineText Value:
      InlineNumber(v-model="fr")
    BlockLine(align="left")
      InlineText Min:
      InlineNumber(v-model="fr")
    BlockLine(align="left")
      InlineCheck(
        :default="false",
        yes="Disabled",
        no="Enabled",
        v-model="isDisabled"
      )
    BlockLine(align="left")
      InlineCheck(
        :default="false",
        yes="Enable Popup",
        no="Disable Popup",
        v-model="isPopup"
      )
    BlockLine(align="left", v-if="isPopup")
      InlineText Popup Text:
      InlineInput(v-model="popupText")
    BlockLine(align="left")
      InlineCheck(
        :default="false",
        yes="Enable Shake",
        no="Disable Shake",
        v-model="isShake"
      )
      InlineCheck(
        v-if="isShake",
        :default="false",
        yes="Shake Forever",
        no="Shake for Mouse",
        v-model="shakeForever"
      )
    BlockLine(align="left")
      InlineText Text RGB:
      InlineInput(type="color", v-model="color")
      InlineText Background RGB:
      InlineInput(type="color", v-model="bgColor")
  BlockPage
    BlockLine(align="left")
      InlineHeading(:level="2") Color
    BlockLine(align="center")
      FilterPopup(:enabled="isPopup", :value="popupText")
        FilterShake(:enabled="isShake", :forever="shakeForever")
          InlineInput(type="color", v-model="color", default="#ffffff")
    BlockLine(align="left")
      InlineText Value:
      InlineNumber(v-model="fr")
    BlockLine(align="left")
      InlineText Min:
      InlineNumber(v-model="fr")
    BlockLine(align="left")
      InlineCheck(
        :default="false",
        yes="Disabled",
        no="Enabled",
        v-model="isDisabled"
      )
    BlockLine(align="left")
      InlineCheck(
        :default="false",
        yes="Enable Popup",
        no="Disable Popup",
        v-model="isPopup"
      )
    BlockLine(align="left", v-if="isPopup")
      InlineText Popup Text:
      InlineInput(v-model="popupText")
    BlockLine(align="left")
      InlineCheck(
        :default="false",
        yes="Enable Shake",
        no="Disable Shake",
        v-model="isShake"
      )
      InlineCheck(
        v-if="isShake",
        :default="false",
        yes="Shake Forever",
        no="Shake for Mouse",
        v-model="shakeForever"
      )
    BlockLine(align="left")
      InlineText Text RGB:
      InlineInput(type="color", v-model="color")
      InlineText Background RGB:
      InlineInput(type="color", v-model="bgColor")
</template>

<style lang="stylus">
html
  background gray
  font-family monospace

body
  width 100vw
  height 100vh
  position relative
</style>

<style lang="stylus" scoped>
.grid-container
  display grid
  grid-template-columns 1fr 1fr

  &>div
    height 50vh
    border .5px solid black

  .center
    display grid
    place-items center

.left, .right
  border .5px solid black
  flex-grow 1
  height 50vh
  display grid
  place-items center

.line
  border-top .1px solid black
</style>

<script lang="ts" setup>
import { defineComponent, ref } from "vue";
const text = ref("Text");
const headingLevel = ref(2);
const isPopup = ref(false);
const isShake = ref(false);
const isDisabled = ref(false);
const shakeForever = ref(false);
const popupText = ref("Popup Text");
const color = ref("#000000");
const bgColor = ref("#ffffff");
const pValue = ref(3);
const min = ref(1);
const max = ref(5);

import Viewport from "./components/Viewport.vue";
import BlockPage from "./components/BlockPage.vue";
import BlockLine from "./components/BlockLine.vue";
import BlockGrid from "./components/BlockGrid.vue";
import InlineHeading from "./components/InlineHeading.vue";
import FilterShake from "./components/FilterShake.vue";
import FilterPopup from "./components/FilterPopup.vue";
import InlineButton from "./components/InlineButton.vue";
import InlineText from "./components/InlineText.vue";
import InlineProgress from "./components/InlineProgress.vue";
import InlineInput from "./components/InlineInput.vue";
import InlineNumber from "./components/InlineNumber.vue";
import InlineCheck from "./components/InlineCheck.vue";
</script>