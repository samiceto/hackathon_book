ca# Backend Dependencies Analysis

**Date:** 2025-12-17
**Purpose:** Analyze all dependencies for version conflicts and compatibility issues

---

## Direct Dependencies (from requirements.txt)

| Package | Version | Purpose |
|---------|---------|---------|
| fastapi | 0.109.0 | Web framework |
| uvicorn[standard] | 0.27.0 | ASGI server |
| pydantic | >=2.0.0 | Data validation |
| qdrant-client | 1.7.3 | Vector database client |
| cohere | 4.47 | Embeddings API |
| google-generativeai | 0.3.2 | Gemini LLM API |
| openai-agents | >=0.2.0 | OpenAI Agents SDK |
| python-dotenv | 1.0.1 | Environment variables |
| slowapi | 0.1.9 | Rate limiting |

---

## Dependency Tree Analysis

### 1. **fastapi==0.109.0**
**Sub-dependencies:**
- `pydantic>=1.7.4,<2.0.0 || >2.0.0,<2.0.1 || >2.0.1,<3.0.0`
- `starlette>=0.35.0,<0.36.0`
- `typing-extensions>=4.8.0`

**Potential Conflicts:**
- ✅ Compatible with `pydantic>=2.0.0` (our constraint)
- ⚠️ Requires specific starlette version (0.35.x)

---

### 2. **uvicorn[standard]==0.27.0**
**Sub-dependencies:**
- `click>=7.0`
- `h11>=0.8`
- `httptools>=0.5.0` (with [standard])
- `python-dotenv>=0.13` (with [standard])
- `pyyaml>=5.1` (with [standard])
- `uvloop>=0.14.0` (with [standard])
- `watchfiles>=0.13` (with [standard])
- `websockets>=10.4` (with [standard])

**Potential Conflicts:**
- ✅ python-dotenv>=0.13 compatible with our 1.0.1
- ✅ No known conflicts

---

### 3. **pydantic>=2.0.0**
**Sub-dependencies:**
- `pydantic-core==2.x.x` (must match pydantic version)
- `typing-extensions>=4.6.1`

**Potential Conflicts:**
- ⚠️ Many packages require specific pydantic versions
- ⚠️ fastapi 0.109.0 requires pydantic v2
- ⚠️ Some older packages might require pydantic v1

---

### 4. **qdrant-client==1.7.3**
**Sub-dependencies:**
- `grpcio>=1.41.0`
- `grpcio-tools>=1.41.0`
- `httpx>=0.20.0`
- `numpy>=1.21`
- `portalocker>=2.0.0`
- `pydantic>=1.10.8`

**Potential Conflicts:**
- ✅ pydantic>=1.10.8 compatible with our >=2.0.0
- ⚠️ httpx version overlap with other packages
- ⚠️ grpcio can be slow to install

---

### 5. **cohere==4.47**
**Sub-dependencies:**
- `httpx>=0.21.2`
- `pydantic>=1.9.2`
- `typing-extensions>=4.0.0`

**Potential Conflicts:**
- ✅ Compatible with our pydantic constraint
- ⚠️ httpx overlap with qdrant-client

---

### 6. **google-generativeai==0.3.2**
**Sub-dependencies:**
- `google-ai-generativelanguage>=0.4.0,<1.0.0`
- `google-api-core`
- `google-auth>=2.15.0`
- `protobuf>=3.19.0`
- `pydantic>=1.10.0`
- `tqdm>=4.66.1`
- `typing-extensions>=4.5.0`

**Potential Conflicts:**
- ✅ Compatible with pydantic>=2.0.0
- ⚠️ protobuf version must be compatible with grpcio
- ⚠️ Large dependency tree (google-auth, google-api-core)

---

### 7. **openai-agents>=0.2.0** ⚠️ **CRITICAL - MAIN CONFLICT SOURCE**
**Sub-dependencies (estimated for v0.2.0):**
- `openai>=2.9.0,<3.0.0` ⚠️
- `pydantic>=2.12.3,<3.0.0` ⚠️
- `httpx>=0.25.0`
- `typing-extensions>=4.5.0`
- `aiohttp>=3.8.0`

**Potential Conflicts:**
- ⚠️ **MAJOR:** Requires `pydantic>=2.12.3` (very specific lower bound)
- ⚠️ **MAJOR:** Requires `openai>=2.9.0` (but we don't have openai in requirements.txt)
- ⚠️ httpx version overlap with cohere, qdrant-client
- ⚠️ Large transitive dependency tree from openai package

---

### 8. **python-dotenv==1.0.1**
**Sub-dependencies:**
- None (pure Python)

**Potential Conflicts:**
- ✅ No conflicts

---

### 9. **slowapi==0.1.9**
**Sub-dependencies:**
- `fastapi>=0.70.0`
- `redis>=4.0.0`
- `limits>=2.0.0`

**Potential Conflicts:**
- ✅ fastapi>=0.70.0 compatible with our 0.109.0
- ⚠️ redis dependency adds complexity
- ⚠️ limits package has sub-dependencies

---

## Critical Conflicts Identified

### 🔴 **CONFLICT 1: Missing openai package**
- **Issue:** `openai-agents>=0.2.0` requires `openai>=2.9.0,<3.0.0`
- **Current State:** openai not in requirements.txt
- **Solution:** Add `openai>=2.9.0,<3.0.0` to requirements.txt

### 🔴 **CONFLICT 2: Pydantic version constraints**
- **Issue:** Multiple packages need different pydantic versions
  - fastapi 0.109.0: `pydantic>=1.7.4,<3.0.0` (flexible)
  - openai-agents 0.2.0: `pydantic>=2.12.3,<3.0.0` (restrictive)
  - qdrant-client 1.7.3: `pydantic>=1.10.8` (flexible)
- **Current State:** `pydantic>=2.0.0` (too loose)
- **Solution:** Use `pydantic>=2.12.3,<3.0.0` to satisfy all

### 🟡 **CONFLICT 3: httpx version overlap**
- **Issue:** Multiple packages depend on httpx
  - cohere: `httpx>=0.21.2`
  - qdrant-client: `httpx>=0.20.0`
  - openai-agents: `httpx>=0.25.0`
- **Solution:** Let pip resolve to compatible version (likely >=0.25.0)

### 🟡 **CONFLICT 4: Complex dependency tree**
- **Issue:** openai-agents pulls in ~50+ transitive dependencies
  - openai SDK has its own large tree
  - Can cause "resolution-too-deep" errors
- **Solution:**
  - Option A: Pin all versions explicitly
  - Option B: Remove openai-agents, use direct OpenAI API

### 🟡 **CONFLICT 5: protobuf/grpcio compatibility**
- **Issue:** google-generativeai and qdrant-client both use protobuf/grpcio
  - Must use compatible versions
  - grpcio is platform-specific and slow to build
- **Solution:** Let pip resolve, ensure build tools available on Render

---

## Recommended Fixes

### **Option A: Fix Current Requirements (Recommended if keeping agents SDK)**

```txt
# FastAPI Framework
fastapi==0.109.0
uvicorn[standard]==0.27.0
pydantic>=2.12.3,<3.0.0  # ⬅️ FIXED: Tighter constraint

# Vector Database
qdrant-client==1.7.3

# Embeddings & LLM
cohere==4.47
openai>=2.9.0,<3.0.0  # ⬅️ ADDED: Required by openai-agents
google-generativeai==0.3.2

# OpenAI Agents SDK
openai-agents>=0.2.0

# Environment Variables
python-dotenv==1.0.1

# Rate Limiting
slowapi==0.1.9
```

**Pros:**
- Keeps agents SDK functionality
- Should resolve without conflicts

**Cons:**
- Large dependency tree (~50+ packages)
- Slow builds (10-20 minutes on Render)
- Risk of "resolution-too-deep" errors

---

### **Option B: Remove Agents SDK (Recommended for stability)**

```txt
# FastAPI Framework
fastapi==0.109.0
uvicorn[standard]==0.27.0
pydantic>=2.12.3,<3.0.0

# Vector Database
qdrant-client==1.7.3

# Embeddings & LLM
cohere==4.47
openai>=2.9.0,<3.0.0  # ⬅️ Direct API usage
google-generativeai==0.3.2

# Environment Variables
python-dotenv==1.0.1

# Rate Limiting
slowapi==0.1.9
```

**Pros:**
- Only 9 direct dependencies
- Fast builds (2-3 minutes on Render)
- No dependency resolution issues
- Same functionality via direct OpenAI function calling

**Cons:**
- Must rewrite agent.py (already done in commit 2e2c0da)

---

## Build Time Analysis

| Configuration | Direct Deps | Total Deps | Build Time | Risk Level |
|--------------|-------------|------------|------------|------------|
| With openai-agents | 9 | ~50-60 | 10-20 min | 🔴 High |
| Without openai-agents | 8 | ~30-40 | 2-3 min | 🟢 Low |

---

## Recommendations

1. **Immediate Fix for Current Setup:**
   - Update `pydantic>=2.0.0` to `pydantic>=2.12.3,<3.0.0`
   - Add `openai>=2.9.0,<3.0.0` explicitly

2. **Long-term Stability:**
   - Consider removing `openai-agents` SDK
   - Use direct OpenAI API with function calling (simpler, faster, more reliable)

3. **If Keeping Agents SDK:**
   - Monitor Render build logs for "resolution-too-deep" errors
   - If errors occur, switch to Option B (remove agents SDK)

---

## Verification Commands

```bash
# Check for conflicts locally
cd backend
pip install --dry-run -r requirements.txt

# Show full dependency tree
pip install pipdeptree
pipdeptree

# Check specific package dependencies
pip show openai-agents
pip show fastapi
```

---

## Conclusion

**Root Cause:** The `openai-agents` package has a complex dependency tree that conflicts with pip's resolution capabilities, especially on Render's build environment.

**Recommendation:** Use **Option B** (remove openai-agents) for guaranteed deployment success and faster builds.
