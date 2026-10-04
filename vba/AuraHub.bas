Attribute VB_Name = "AuraHub"
Option Explicit

Public Sub Aura_Start()
    MsgBox "Aura Hub is starting. Canonical source: workbook/Aura.xlsl", vbInformation, "Aura Hub"
End Sub

Public Sub Aura_Simulate()
    MsgBox "Simulation action selected. Execute only explicitly enabled XLSL simulations.", vbInformation, "Aura Hub"
End Sub

Public Sub Aura_Visualize()
    MsgBox "Visualization action selected.", vbInformation, "Aura Hub"
End Sub

Public Sub Aura_Deploy()
    MsgBox "Deployment action selected. Verify provenance before publishing.", vbInformation, "Aura Hub"
End Sub

Public Sub Aura_Ethics()
    MsgBox "Review assumptions, evidence state, and epistemic status before interpreting results.", vbInformation, "Aura Hub"
End Sub

Public Sub Aura_LMLM()
    MsgBox "LMLM profiles: lmlm-default, lmlm-reasoner, lmlm-code, lmlm-vision.", vbInformation, "Aura LMLM"
End Sub

Public Sub Aura_Status()
    MsgBox "Aura XLSL projection is available. LMLM is configured through the provider adapter.", vbInformation, "Aura Hub"
End Sub

Public Sub Build_Home_UI()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Home")
    ws.Cells.Clear
    ws.Range("B2").Value = "Aura Hub - Research Ecosystem"
    ws.Range("B2").Font.Size = 18
    ws.Range("B2").Font.Bold = True
    AddButton ws, "Start Aura", "Aura_Start", 4
    AddButton ws, "Run Simulation", "Aura_Simulate", 6
    AddButton ws, "Visualize Data", "Aura_Visualize", 8
    AddButton ws, "Deploy", "Aura_Deploy", 10
    AddButton ws, "Ethics Notes", "Aura_Ethics", 12
    AddButton ws, "LMLM Models", "Aura_LMLM", 14
    AddButton ws, "Status Check", "Aura_Status", 16
End Sub

Private Sub AddButton(ByVal ws As Worksheet, ByVal txt As String, ByVal macro As String, ByVal row As Long)
    Dim btn As Shape
    Set btn = ws.Shapes.AddShape(msoShapeRoundedRectangle, 100, row * 20, 220, 30)
    btn.TextFrame.Characters.Text = txt
    btn.OnAction = macro
    btn.Fill.ForeColor.RGB = RGB(0, 102, 204)
    btn.TextFrame.Characters.Font.Color = RGB(255, 255, 255)
    btn.TextFrame.Characters.Font.Bold = True
End Sub
