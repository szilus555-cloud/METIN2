# Template Images Directory

This directory should contain template images used for image recognition in the dungeon automation script.

## Required Images

Create the following screenshots from the game and save them as PNG files in this directory:

### 1. `dungeon_npc.png`
Screenshot of the NPC that allows entering the dungeon. Should include distinctive visual features of the NPC.

**How to create:**
1. Stand in front of the dungeon entrance NPC
2. Take a screenshot
3. Crop to show only the NPC (approximately 100x100 to 200x200 pixels)
4. Save as `dungeon_npc.png`

### 2. `enter_button.png`
Screenshot of the "Enter" or "Start" button that appears in the dungeon entry dialog.

**How to create:**
1. Open the dungeon entry dialog
2. Take a screenshot
3. Crop to show only the enter/start button
4. Save as `enter_button.png`

### 3. `enemy_indicator.png`
Screenshot showing the enemy name/health bar or visual indicator that appears above enemies.

**How to create:**
1. Target an enemy in the game
2. Take a screenshot
3. Crop to show the enemy indicator (name/health bar)
4. Save as `enemy_indicator.png`

### 4. `dungeon_complete.png`
Screenshot of the completion notification or any distinctive element that appears when dungeon is completed.

**How to create:**
1. Complete a dungeon
2. Take a screenshot of the completion notification
3. Crop to show the distinctive completion element
4. Save as `dungeon_complete.png`

### 5. `exit_portal.png`
Screenshot of the exit portal that appears after dungeon completion.

**How to create:**
1. Find the exit portal after completing a dungeon
2. Take a screenshot
3. Crop to show the portal
4. Save as `exit_portal.png`

## Image Guidelines

- **Format:** PNG (recommended for best quality)
- **Size:** Keep templates reasonably small (100x100 to 300x300 pixels)
- **Quality:** Clear, not blurry
- **Lighting:** Should match typical in-game lighting
- **Resolution:** Match your game resolution (1920x1080 recommended)

## Tips for Best Results

1. **Distinctive features:** Choose parts of the UI that are unique and easily recognizable
2. **Avoid animations:** Capture static elements, not animated ones
3. **Clean captures:** No overlapping UI elements if possible
4. **Multiple angles:** You may want to create multiple versions if elements appear differently
5. **Testing:** Test each template image with lower confidence values first

## Testing Individual Images

You can test if your images are being recognized by temporarily adding debug output to the script or by adjusting the `confidence` parameter in `config.json`.

- Start with `confidence: 0.8` (default)
- If images aren't recognized, try lowering to `0.7` or `0.6`
- If too many false positives, increase to `0.85` or `0.9`

## Example Directory Structure

```
images/
├── README.md (this file)
├── dungeon_npc.png
├── enter_button.png
├── enemy_indicator.png
├── dungeon_complete.png
└── exit_portal.png
```

---

**Note:** The automation script will not work without these template images. Make sure to create them before running the script.
