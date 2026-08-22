# Rename map — public labels → KBMill

**Goal:** Strangers and models never think VF is the product.  
**Point of sale:** https://kbmill.com  

Copy already says KBMill. This doc is the **slug / surface** rename plan.

## Layers (outside → inside)

| # | Layer | Today | Target | Who |
|---|--------|--------|--------|-----|
| 1 | **Site** | kbmill.com | Keep | Done |
| 2 | **Public copy** | README / Notes / FAQ | KBMill-only | Done (pushed) |
| 3 | **X** | @VectorForgePro | Display **KBMill**, website kbmill.com; handle `@kbmill` later if free | Carroll in app |
| 4 | **GitHub library** | `CMiller56/vf-brick-library` | `CMiller56/kbmill-library` (GitHub keeps redirect) | Carroll click + link sweep |
| 5 | **HF dataset** | `CMiller/vf-brick-retrieval` | `CMiller/kbmill-retrieval` (or `kbmill/…` if org) | Carroll HF Settings + re-upload card |
| 6 | **Brick ZIP / card prose** | Some “VF Pro” footers in demos | KBMill / plant | Sweep after 4–5 |
| 7 | **BRICK_SPEC optional runtime** | “without VectorForge” | “without the plant runtime” / “any loader” | Soft copy |
| 8 | **Pro monorepo** | `VectorForge-Pro`, pkg `vectorforge_pro` | **Keep internal** for now | Later / never for strangers |
| 9 | **Engine** | `VectorForge-Project` / `vectorforge` | **Keep internal** | Later |
| 10 | **PyPI / wheels** | none public for mill | If published: `kbmill` | Future |

## Recommended next clicks (4 → 5)

### GitHub rename
1. Open https://github.com/CMiller56/vf-brick-library/settings  
2. **Repository name** → `kbmill-library`  
3. Leave **“Redirect will be created”** on  
4. Update local remote:
   ```bash
   cd ~/Desktop/vf-brick-library
   git remote set-url origin git@github.com:CMiller56/kbmill-library.git
   ```
5. Grep-replace public docs that *display* the old slug (URLs to old repo still redirect)

### Hugging Face rename
1. Dataset Settings → rename to `kbmill-retrieval` **or** create new dataset and mark old as redirected in README  
2. Push updated card from `hf_datasets/vf-brick-retrieval/` (folder name can stay until rebuild script updates)  
3. Update library README link to new dataset id  

### X
- Name: KBMill · Website: https://kbmill.com · Bio as in brand push notes  
- Handle rename only if `@kbmill` is available and worth the break  

## What we are *not* renaming this week
- Private `VectorForge-Pro` / Engine package paths  
- Local `hopper_work` / plant folder names  
- Historical commits and old tweets (they become history)

## Success
A frontier model or contract team searches / cites **KBMill** and lands on **kbmill.com**. Proof links may still say `kbmill-library` on GitHub — never “buy VectorForge.”
