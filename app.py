campos_obrigatorios = [empresa, cnpj, rua, ...]

# Adiciona validação de responsável apenas para Dr. Adão
if medico == "Adão Rinede Alves de Almeida":
    campos_obrigatorios.extend([responsavel, funcao])
```

**Resultado:** Valida responsável **somente** se for Dr. Adão.

---

### **3. Textos Diferentes por Médico (Linha 118-163)**

#### **Dr. Adão (assinado pelo responsável da empresa):**
```
DECLARAÇÃO

[Empresa], [CNPJ], ..., representada por [Responsável]
([Função]), DECLARO que [Dr. Adão] é responsável...

_________________________
Responsável (ass. digital)
```

#### **Dr. Odilon (assinado pelo próprio médico):**
```
DECLARAÇÃO

Eu, ODILON BATISTA SOARES, ..., DECLARO que sou responsável
pela coordenação ... da empresa [Empresa], [CNPJ], ...

_________________________
Dr. Odilon Batista Soares
CREMESC 4195 – RQE 3249
