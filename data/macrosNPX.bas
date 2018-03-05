Attribute VB_Name = "Module1"
Sub CleanPtBrChars()

Dim toRemove()
Dim toReplace()
Dim listLB As Integer
Dim listUB As Integer
Dim rng As Range

toRemove() = Array("Ç", "Á", "É", "Í", "Ó", "Ú", "Ã", "Õ", "Â", "Ê", "À")
toReplace() = Array("C", "A", "E", "I", "O", "U", "A", "O", "A", "E", "A")

listUB = UBound(toRemove)
listLB = LBound(toRemove)

For itm = listLB To listUB
    For Each iCell In ActiveSheet.UsedRange
        iCell.Replace What:=toRemove(itm), Replacement:=toReplace(itm), MatchCase:=False
    Next iCell
Next itm
End Sub

Sub Comma2Dot()
For Each iCell In Selection
    iCell.Replace What:=",", Replacement:=".", MatchCase:=True
Next iCell
End Sub

Sub Dot2Comma()
For Each iCell In Selection
    iCell.Replace What:=".", Replacement:=",", MatchCase:=True
Next iCell
End Sub
